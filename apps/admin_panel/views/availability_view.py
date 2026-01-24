from django.shortcuts import render
from django.views import View
from apps.docbook.services import appointment_services, availability_services
from apps.doctors.services import department_services
from apps.doctors.services import doctor_services
from apps.core.utilities.decorators import admin_required

from pprint import pprint

@admin_required(login_url="/admin/login/")
class DoctorsSchedulesView(View):
    def get(self, request):
        todays_appointments = appointment_services.todays_appointments_count_for_all_doctors()
        doctor_on_duty = availability_services.today_active_doctors_count()
        available_time_slots = availability_services.today_doctor_available_slots()
        emergency_cases = appointment_services.todays_emergency_appointments_count()
        departments = department_services.get_all_departments()
        appointment_types_status = appointment_services.get_all_appointment_types_status()
        
        start_date, end_date = availability_services.get_current_week_range()
        
        doctors_appointments_today = appointment_services.doctors_appointments_today()
        doctors_appointments_by_week = appointment_services.doctors_appointments_in_current_week(start_date=start_date, end_date=end_date)
        
        doctors = doctor_services.get_all_doctors()

        context={
            "todays_appointments": todays_appointments,
            "doctor_on_duty": doctor_on_duty,
            "available_time_slots": available_time_slots,
            "emergency_cases": emergency_cases,
            "doctors_appointments_today": doctors_appointments_today,
            "doctors_appointments_by_week": doctors_appointments_by_week,
            "departments": departments,
            "doctors": doctors,
            "appointment_types": appointment_types_status['types'],
            "appointment_status": appointment_types_status['statuses'],
        }
        

        pprint(context)


        return render(request, "admin/doctors/doctor_schedules.html", context)
    
     

@admin_required(login_url="/admin/login/")
class DoctorSchedulesView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_schedules.html")