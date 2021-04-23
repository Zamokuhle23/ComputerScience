from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth')
    gender = models.CharField(max_length=20)
    REQUIRED_FIELDS = ["name", "gender"]

class Post(models.Model):
    date_created = models.DateTimeField('date published')
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=9000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    num_likes = models.IntegerField()


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


