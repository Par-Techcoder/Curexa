from apps.accounts import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.accounts.views.admin_user_viewset import AdminUserViewSet

router = DefaultRouter()
router.register(r'admin-users', AdminUserViewSet, basename='admin-users')

urlpatterns = [
    path('', include(router.urls)), 
    # Home URL
    path('', views.HomeView.as_view(), name='home'),
    
    # Authentication URLs
    # path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    
    
]

