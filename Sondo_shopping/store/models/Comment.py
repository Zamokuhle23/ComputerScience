import datetime
from django.db import models
from users.models import User
from django.urls import reverse

from store.models import Product


class Comment(models.Model):
    text = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png', upload_to='profile_pics')
    product_connected = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.text


    def get_absolute_url(self):
        return reverse('product-detail',kwargs={'pk':self.product_connected.id})