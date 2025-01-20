from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if not cart_items.exists():
                        messages.error(request, 'Ваша корзина пуста. Добавьте товары в корзину, чтобы оформить заказ.')
                        return redirect('cart:view')  # Assuming you have a cart view

                    # Create the order
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get'],
                    )

                    # Create the order items
                    for cart_item in cart_items:
                        product = cart_item.product
                        name = cart_item.product.name
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(
                                f'Недостаточное количество товара "{name}" на складе. В наличии - {product.quantity}'
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )

                        # Update the product quantity in stock
                        product.quantity -= quantity
                        product.save()

                    # Clear the user's cart after order is created
                    cart_items.delete()

                    messages.success(request, 'Ваш заказ оформлен успешно!')
                    return redirect('user:profile')

            except ValidationError as e:
                messages.error(request, str(e))  # Using error instead of success for validation
                return redirect('cart:order')  # Redirect to the order page to fix the issue

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)
