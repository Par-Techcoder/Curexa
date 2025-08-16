from django.views import View
from django.shortcuts import render, redirect


class AdminDashboardView(View):
    def get(self, request):
        # Logic for rendering the admin dashboard
        return render(request, 'admin/base.html')

class MedicationListView(View):
    def get(self, request):
        # Logic for listing medications
        return render(request, 'admin/medicens/medication_list.html')    
