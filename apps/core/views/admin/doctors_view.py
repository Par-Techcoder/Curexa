from django.views import View
from django.shortcuts import render, redirect

class DoctorListView(View):
    def get(self, request):
        return render(request, "admin/doctors/doctors_list.html")
    

class DoctorAddView(View):
    def get(self, request):
        return render(request, "admin/doctors/doctor_add.html")
    
    def post(self, request):
        # Handle form submission logic here
        return redirect("doctor_list")    
    
class DoctorSchedulesView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_schedules.html")    