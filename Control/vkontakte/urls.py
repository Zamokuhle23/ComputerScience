from django.urls import path, include
#from .views import
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from . import views
from .views import PostViewSet, LikesViewSet, UserViewSet

schema_views = get_swagger_view(title='Posts')
router = DefaultRouter()
router1 = DefaultRouter()
router2 = DefaultRouter()
router.register(r"users",views.UserViewSet,"users")
router1.register(r"posts",views.PostViewSet,"posts")
router2.register(r"likes",views.LikesViewSet,"likes")

urlpatterns = [
    path('posts/', include(router1.urls)),
    path('likes/', include(router2.urls)),
    path('users/', include(router.urls)),
    path('',schema_views),
    path("posts/<int:id>/likes",PostViewSet.as_view({'get': 'get_likes'})),
    ]