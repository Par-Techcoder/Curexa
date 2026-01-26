from django.shortcuts import render
from django.views import View
from apps.docbook.services import appointment_services, availability_services
from apps.doctors.services import department_services
from apps.doctors.services import doctor_services
from apps.core.utilities.decorators import admin_required
from apps.core.constants.default_values import DOCTOR_TIME_SLOTS


@admin_required(login_url="/admin/login/")
class DoctorsSchedulesView(View):
    def get(self, request):
        # ---------------------------
        # KPIs
        # ---------------------------
        todays_appointments = appointment_services.todays_appointments_count_for_all_doctors()
        doctor_on_duty = availability_services.today_active_doctors_count()
        available_time_slots = availability_services.today_doctor_available_slots()
        emergency_cases = appointment_services.todays_emergency_appointments_count()

        # ---------------------------
        # Filters & Types
        # ---------------------------
        departments = department_services.get_all_departments()
        appointment_types_status = appointment_services.get_all_appointment_types_status()

        doctors = doctor_services.get_all_doctors()
        # ---------------------------
        # Context
        # ---------------------------
        context = {
            "todays_appointments": todays_appointments,
            "doctor_on_duty": doctor_on_duty,
            "available_time_slots": available_time_slots,
            "emergency_cases": emergency_cases,
            "doctors": doctors,
            "departments": departments,            
            "appointment_types": appointment_types_status["types"],
            "appointment_status": appointment_types_status["statuses"],
            "time_slots": DOCTOR_TIME_SLOTS,
        }

        return render(request, "admin/doctors/doctor_schedules.html", context)


    
     

@admin_required(login_url="/admin/login/")
class DoctorSchedulesView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_schedules.html")