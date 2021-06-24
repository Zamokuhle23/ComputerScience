#from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


class Customer(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=30,default='shopping12345')
    def __str__(self):
        return f'{self.customer.username} Customer'
    def save(self):
        self.customer.is_customer = True
        super().save()
    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    @staticmethod
    def emailExits(userEmail):
        try:
            email = Customer.objects.get(email=userEmail)
            return email.customer
        except:
            return False



