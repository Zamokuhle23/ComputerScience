from django.contrib.auth.models import User
from django.template.loader import render_to_string
from celery import shared_task
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# from djcelery_email.tasks import send_email
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from Sondo_shopping.settings import EMAIL_HOST_USER
from customers.models import Customer
from store.models import Order


@shared_task
def SendResetPassword(subject=None,email=None,user_email=None):
    # user = User.objects.get(email=user_email)
    # subject = "Password Reset Requested"
    # email_template_name = "password_reset_email.txt"
    # c = {
    #     "email": user_email,
    #     'domain': '127.0.0.1:8000',
    #     'site_name': 'Website',
    #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
    #     "user": user,
    #     'token': default_token_generator.make_token(user),
    #     'protocol': 'http',
    # }
    # email = render_to_string(email_template_name, c)
    # print("EMail Sent To: " + user_email)
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
