from apps.core.views import admin as views
from django.urls import path

urlpatterns = [
    # Authentication
    path("admin/login/", views.AdminLoginView.as_view(), name="admin_login"),
    path("admin/logout/", views.AdminLogoutView.as_view(), name="admin_logout"),

    # Dashboard
    path("admin/", views.AdminDashboardView.as_view(), name="admin_dashboard"),
    
    # Doctors
    path("admin/doctors/", views.DoctorListView.as_view(), name="doctor_list"),
    path("admin/doctors/add/", views.DoctorAddView.as_view(), name="doctor_add"),
    path("admin/doctors/<int:pk>/schedules/", views.DoctorSchedulesView.as_view(), name="doctor_schedles"),
    
    # Patients
    path("admin/patients/", views.PatientListView.as_view(), name="patient_list"),
    path("admin/patients/add/", views.PatientAddView.as_view(), name="patient_add"),
    path("admin/patients/<int:pk>/medical-records/", views.PatientMedicalRecordsView.as_view(), name="patient_medical_records"),
    
    # Appointments
    path("admin/appointments/", views.AppointmentListView.as_view(), name="appointment_list"),
    path("admin/appointments/appointment-history/", views.AppointmentHistoryView.as_view(), name="appointment_history"),
    path("admin/appointments/add/", views.AppointmentAddView.as_view(), name="appointment_add"),

    # Medicines
    path("admin/medicines/", views.MedicineListView.as_view(), name="medicine_list"),
    path("admin/medicines/add/", views.MedicineAddView.as_view(), name="medicine_add"),
    path("admin/medicines/<int:pk>/edit/", views.MedicineEditView.as_view(), name="medicine_edit"),
    
    # Categories
    path("admin/categories/", views.CategoryListView.as_view(), name="category_list"),
    
    # Inventory
    path("admin/inventory/", views.InventoryListView.as_view(), name="inventory_list"),
    
]

