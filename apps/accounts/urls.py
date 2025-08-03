from apps.accounts import views
from django.urls import path

urlpatterns = [
    
    # Home URL
    path('', views.HomeView.as_view(), name='home'),
    
]

