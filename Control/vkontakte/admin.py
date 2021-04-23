from django.contrib import admin

# Register your models here.
from vkontakte.models import User, Post, Likes

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Likes)
