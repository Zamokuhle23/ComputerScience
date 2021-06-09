from rest_framework import serializers

from vkontakte.models import Post, User, Likes


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","body"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ["id","name","date_of_birth"]

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields  = ["id","user","num_likes"]