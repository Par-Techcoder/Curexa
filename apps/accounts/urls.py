from apps.accounts import views
from django.urls import path

urlpatterns = [
    
    # Home URL
    path('', views.HomeView.as_view(), name='home'),
    
    # Authentication URLs
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    
    
]

