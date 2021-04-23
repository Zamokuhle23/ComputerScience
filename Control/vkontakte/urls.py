from django.urls import path
#from .views import
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(),name='home'),

    ]