from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import (
    home, register, profile
)

urlpatterns = [
    path('', home, name='home-page'),

    path('profile/', profile, name='profile-page'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', register, name='signup-page'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)