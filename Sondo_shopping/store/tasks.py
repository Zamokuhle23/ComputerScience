import random

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail


from Sondo_shopping.settings import EMAIL_HOST_USER
from customers.models import Customer
from store.models import Order, Product


@shared_task
def SendResetPassword(subject=None, email=None, user_email=None):

    send_mail(subject, email, EMAIL_HOST_USER, [user_email], fail_silently=False)


@shared_task
def OrderEmail(order_id=None):
    order = Order.objects.get(id=order_id)

    customer = Customer.objects.get(id=order.customer.id)
    print("Sending Email to " + customer.customer.email)
    send_mail(
        'Order on Sondo_shopping',
        'Thank You for placing Order, %s on its way.' % order.product.name,
        EMAIL_HOST_USER,
        [customer.customer.email],
        fail_silently=False,
    )

@shared_task
def SendAdvert():
    customers = User.objects.all()
    products = Product.objects.all()
    product = random.choice(tuple(products))
    customer = random.choice(tuple(customers))
    send_mail(
        'Order on Sondo_shopping',
        f'Thank You for placing Order, {product.name} {product.image} on its way.',
        EMAIL_HOST_USER,
        [customer.email],
        fail_silently=False,
    )



