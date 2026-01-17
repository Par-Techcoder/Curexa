from django.views import View
from django.shortcuts import render, redirect
from apps.doctors.services import doctor_services
from apps.docbook.services import availabilities_services

class DoctorListView(View):
    def get(self, request):
        doctors = doctor_services.doctor_list()
        total_doctors = doctor_services.total_doctors_count()
        specialized_doctors  = doctor_services.specialized_doctors_count()
        active_doctors = availabilities_services.today_active_doctors_count()
        inactive_doctors_today = total_doctors - active_doctors
        context = {
            "doctors": doctors,
            "total_doctors": total_doctors,
            "specialized_doctors": specialized_doctors,
            "active_doctors": active_doctors,
            "inactive_doctors_today": inactive_doctors_today,
        }
        return render(request, "admin/doctors/doctors_list.html", context)
    

class DoctorAddView(View):
    def get(self, request):
        return render(request, "admin/doctors/doctor_add.html")
    
    def post(self, request):
        name=request.POST.get("name"),
        specialization=request.POST.get("specialization"),
        email=request.POST.get("email"),
        phone=request.POST.get("phone"),
        
        doctor_services.doctor_add(name, specialization, email, phone)
        return redirect("doctor_list")    
    
class DoctorSchedulesView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_schedules.html")    
    
class DoctorDetailView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_detail.html")    
    
    
class DoctorEditView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_edit.html")    