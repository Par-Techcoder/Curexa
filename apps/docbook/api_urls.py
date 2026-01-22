from django.urls import path
from apps.docbook import views

urlpatterns = [
    # Availability
    path('availability/create/', views.AvailabilityCreateAPIView.as_view(), name='admin-availability-create'),
    
    # Appointments
    path('appointments/book/', views.AppointmentBookAPIView.as_view(), name='admin-appointment-book'),
]
