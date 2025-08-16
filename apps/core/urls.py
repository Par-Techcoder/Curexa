from apps.core import views
from django.urls import path

urlpatterns = [
    
    # Admin URLs
    path('admin/login', views.AdminLoginView.as_view(), name='admin_login'),
    path('admin/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/medi', views.MedicationListView.as_view(), name='medication_list'),
    path('admin/medi/edit', views.MedicationEditView.as_view(), name='medication_edit'),
    path('admin/medi/add', views.MedicationAddView.as_view(), name='medication_add'),
    
]

