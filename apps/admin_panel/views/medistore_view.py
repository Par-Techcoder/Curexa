from django.views import View
from django.shortcuts import render, redirect
from apps.medistore.services import category_services
from apps.core.services import util_services
from apps.medistore.services import medicine_services
from apps.core.constants.default_values import DosageForm, AGE_GROUP
from apps.core.utilities import file_management

class MedicineListView(View):
    def get(self, request):
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
        categories = category_services.get_all_category()
        context = {
            "categories": categories,
            "dosage_form": util_services.enum_choices(DosageForm),
            "age_group": util_services.enum_choices(AGE_GROUP)
        }
        return render(request, 'admin/medicens/add_new_medication.html', context)

    def post(self, request):
        # 1. Basic Info
        name = request.POST.get('name')
        SKU = request.POST.get('SKU')
        category_id = request.POST.get('category')
        manufacturer = request.POST.get('manufacturer')

        # 2. Pricing & Inventory
        cost_price = request.POST.get('cost_price') or 0
        retail_price = request.POST.get('retail_price') or 0
        change_quantity = request.POST.get('change_quantity') or 0
        stock_alert = request.POST.get('stock_alert') or 0

        # 3. Product Details
        description = request.POST.get('description')
        is_prescription_required = request.POST.get('is_prescription_required') == 'true'
        classification = request.POST.get('classification')
        age_group = request.POST.get('age_group')
        salt_composition = request.POST.get('salt_composition')
        dosage_strength = request.POST.get('dosage_strength')
        manufacture_date = request.POST.get('manufacture_date') or None
        expiry_date = request.POST.get('expiry_date') or None

        # 4. Images (base64 from JS)
        images_data = request.POST.getlist('medicine_images[]')
        
        # Save images
        images_path=file_management.save_uploaded_file(images_data, "Medicine")

        # Save medicine instance
        medicine = medicine_services.add_new_medicine(SKU, name, cost_price, retail_price, images_path, is_prescription_required, category, classification, age_group, salt_composition, dosage_strength, manufacturer, manufacture_date, description, expiry_date)

        
        

        return redirect('medicine_list')
