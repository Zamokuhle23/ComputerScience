from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import PasswordResetCompleteView

from customers import views as user_views
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from Sondo_shopping import views as passwordViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('register/', user_views.register, name='register'),
    #url('^accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                       name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                      template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
                      template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", passwordViews.password_reset_request, name="password_reset"),


    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path("/api/rst-auth/registration/",include("rest_auth.registration.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
