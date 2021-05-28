from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from . import views
from django.urls import path, re_path
from .views import Home,Signup,logout,Cart,Checkout,OrderView
from .middlewares import LoginCheckMiddleware

from .views.home import CommentUpdateView, CommentDeleteView, ProductDetailView

schema_views = get_swagger_view(title='Online Shopping API')
router = DefaultRouter()
router1 = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()
router4 = DefaultRouter()

router1.register(r"categories",views.CategoryViewSet,"categories")
router2.register(r"comments",views.CommentViewSet,"comments")
router3.register(r"orders",views.OrderViewSet,"orders")
router4.register(r"products",views.ProductViewSet,"products")
router.register(r"customers",views.CustomerViewSet,"customers")

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('customers/', include(router.urls)),
    path('categories/', include(router1.urls)),
    path('comments/', include(router2.urls)),
    path('orders/', include(router3.urls)),
    path('products/', include(router4.urls)),

    path('api/',schema_views),
    path('search/', Home.as_view(),name='search'),
    path('signup',Signup.as_view(), name='signup'),
    #path('login',Login.as_view(), name='login'),
    re_path(r"^home/$", views.Home.as_view(), name="home"),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',LoginCheckMiddleware(Cart.as_view()), name='cart'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
    # path('create/<str:content_type>/<int:object_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
