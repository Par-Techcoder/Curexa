from django.views import View
from django.shortcuts import render, redirect

class MedicineListView(View):
    def get(self, request):
        # Logic for listing medications
        return render(request, 'admin/medicens/medication_list.html')    
    
class MedicineEditView(View):
    def get(self, request, pk):
        # Logic for editing a medication
        return render(request, 'admin/medicens/medication_details_edit.html')
    
    def post(self, request, pk):
        # Logic for saving the edited medication
        # This would typically involve form processing and saving to the database
        return redirect('medication_list')    

class MedicineAddView(View): 
    def get(self, request):
        # Logic for adding a new medication
        return render(request, 'admin/medicens/add_new_medication.html')
    
    def post(self, request):
        # Logic for saving the new medication
        # This would typically involve form processing and saving to the database
        return redirect('medication_list')