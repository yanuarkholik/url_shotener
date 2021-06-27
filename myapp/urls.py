from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import (
    home, 
    url,
    edit,
    register, 
    profile, 
    edit_profile, 
    payment, 
    brand, 
    postAJAX, 
    redirect_url_view,
    create,
    create_main,
    validate_username,
)

urlpatterns = [
    path('', home, name='home-page'),
    path('post/ajax/url/', postAJAX, name = "post-ajax"),
    path('profile/edit/', edit_profile, name='edit_profile-page'),
    path('payment/', payment, name='payment-page'),
    path('brand/', brand, name='brand-page'),
    path('profile/', profile, name='profile-page'),

    path('urls/', url, name='url-page'),
    path('create/', create, name='create'),
    path('edit/', edit, name='edit'),
    path('create/main/', create_main, name='create-main'),

    path('signup/', register, name='signup-page'),
    path('validate/', validate_username, name='validate-username'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout-page'),
    path('<slug:slug>/', redirect_url_view, name='redirect-page'),
    
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)