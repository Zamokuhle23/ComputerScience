from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date_of_birth')
    gender = models.CharField(max_length=20)
    REQUIRED_FIELDS = ["name", "gender"]

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_likes = models.IntegerField()

class Post(models.Model):
    date_created = models.DateTimeField('date published')
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=9000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE)





