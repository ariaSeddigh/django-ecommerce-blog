from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.subscription_list, name='subscription_list'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('purchase/', views.purchase_subscription, name='purchase'),
    path('purchase/success/', views.purchase_success, name='purchase_success'),
    path('my-purchases/', views.user_purchases, name='user_purchases'),

]
