from apps.core.views import admin as views
from django.urls import path

urlpatterns = [
    # Authentication
    path("admin/login/", views.AdminLoginView.as_view(), name="admin_login"),
    path("admin/logout/", views.AdminLogoutView.as_view(), name="admin_logout"),

    # Dashboard
    path("admin/", views.AdminDashboardView.as_view(), name="admin_dashboard"),

    # Medicines
    path("admin/medicines/", views.MedicineListView.as_view(), name="medicine_list"),
    path("admin/medicines/add/", views.MedicineAddView.as_view(), name="medicine_add"),
    path("admin/medicines/<int:pk>/edit/", views.MedicineEditView.as_view(), name="medicine_edit"),
]

