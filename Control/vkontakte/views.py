from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from vkontakte.models import Post, User, Likes
from vkontakte.serializers import PostSerializer, UserSerializer, LikesSerializer



class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    def get_likes(self,request,id):
        post = Post.objects.get(id=id)
        return Response({'Likes':post.likes.num_likes})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

class LikesViewSet(viewsets.ModelViewSet):
    serializer_class = LikesSerializer
    def get_queryset(self):
        return Likes.objects.all()