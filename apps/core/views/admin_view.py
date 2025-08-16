from django.views import View
from django.shortcuts import render, redirect


class AdminLoginView(View):
    def get(self, request):
        # Logic for rendering the admin login page
        return render(request, 'admin/auth/admin_login.html')

    def post(self, request):
        # Logic for handling admin login
        # This would typically involve authentication checks
        return redirect('admin_dashboard')

class AdminDashboardView(View):
    def get(self, request):
        # Logic for rendering the admin dashboard
        return render(request, 'admin/base.html')

class MedicationListView(View):
    def get(self, request):
        # Logic for listing medications
        return render(request, 'admin/medicens/medication_list.html')    
    
class MedicationEditView(View):
    def get(self, request):
        # Logic for editing a medication
        return render(request, 'admin/medicens/medication_details_edit.html')
    
    def post(self, request):
        # Logic for saving the edited medication
        # This would typically involve form processing and saving to the database
        return redirect('medication_list')    

class MedicationAddView(View): 
    def get(self, request):
        # Logic for adding a new medication
        return render(request, 'admin/medicens/add_new_medication.html')
    
    def post(self, request):
        # Logic for saving the new medication
        # This would typically involve form processing and saving to the database
        return redirect('medication_list')