from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


# Create your views here.
from vkontakte.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'vkontakte/home.html'
    context_object_name = 'posts'

    ordering = ['date_created']

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/home'


class PostCreateView(CreateView):
    model = Post
    fields = ['title','body']

def like(request, postid, Likes):
    like = Likes()
    obj = ''
    valueobj = ''

    if request.method == "POST":
        post = get_object_or_404(Post, id=postid)
        liker = request.user
        obj = Likes.objects.get(user=request.user, post=post)
        valueobj = obj.value
        valueobj = int(valueobj)
        if obj.user != liker:

            like.user = liker

            like.post = post

            post.num_likes += 1
        else:
            post.num_likes -= 1




