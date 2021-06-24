from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)
    is_deliverman = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'

    @staticmethod
    def emailExits(userEmail):
        try:
            user = User.objects.get(email=userEmail)
            return user.email
        except:
            return False


class Seller(models.Model):
    seller = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

class Producer(models.Model):
    producer = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

class DeliverMan(models.Model):
    deliver = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

class Shipper(models.Model):
    shipper = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png',upload_to='profile_pics')
    email = models.EmailField(max_length=255)

#
# @receiver(post_save, sender=User)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(customer=instance)
#
#
# @receiver(post_save,sender=User)
# def save_customer(sender,instance,created,**kwargs):
#     instance.customer.save()