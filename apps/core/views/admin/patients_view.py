from django.views import View
from django.shortcuts import render, redirect

class PatientListView(View):
    def get(self, request):
        
        return render(request, "admin/patients/patients_list.html")