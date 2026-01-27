from django.views import View
from django.shortcuts import render, redirect
from apps.accounts.services import patient_services

class PatientListView(View):
    def get(self, request):
        patients = patient_services.all_patients()
        return render(request, "admin/patients/patients_list.html", {'patients':patients})
    
class PatientAddView(View):
    def get(self, request):
        # gender = 
        return render(request, "admin/patients/patient_add.html")
    
    def post(self, request):
        # Handle form submission logic here
        return redirect("patient_list")    

class PatientMedicalRecordsView(View):
    def get(self, request, pk):
        return render(request, "admin/patients/patient_medical_recorrds.html")    