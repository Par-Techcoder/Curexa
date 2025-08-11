from apps.core import views
from django.urls import path

urlpatterns = [
    
    # Admin URLs
    path('admin/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    
]

