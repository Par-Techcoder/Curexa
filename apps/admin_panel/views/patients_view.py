from django.views import View
from django.shortcuts import render, redirect

class PatientListView(View):
    def get(self, request):
        
        return render(request, "admin/patients/patients_list.html")
    
class PatientAddView(View):
    def get(self, request):
        return render(request, "admin/patients/patient_add.html")
    
    def post(self, request):
        # Handle form submission logic here
        return redirect("patient_list")    

class PatientMedicalRecordsView(View):
    def get(self, request, pk):
        return render(request, "admin/patients/patient_medical_recorrds.html")    