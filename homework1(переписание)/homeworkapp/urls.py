from django.urls import path
from . import views
from .views import Show

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('show', Show.as_view(),name='show'),
    path('employee/delete/<pk>',views.DeleteView.as_view(),name='employee-delete'),
    path('employee/edit/<pk>',views.UpdateView.as_view(),name='employee-edit'),
    path('employee/',views.CreateView.as_view(),name='employee-create'),
]