from django.db import models
from django.contrib.auth.models import User


# class User(AbstractUser):
#     CUSTOMER = 1
#     SELLER = 2
#
#     ROLE_CHOICES = (
#         (CUSTOMER, 'Customer'),
#         (SELLER, 'Seller'),
#     )
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class Seller(models.Model):
    seller = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

class Producer(models.Model):
    producer = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

class DeliverMan(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

class Shipper(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)