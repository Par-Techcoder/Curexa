from django.views import View
from django.shortcuts import render, redirect
from apps.doctors.services import doctor_services, department_services, specialization_services, qualification_services
from apps.docbook.services import availabilities_services
from apps.accounts.services import user_services
from apps.core.utilities.file_management import save_uploaded_file

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
        departments = department_services.get_all_departments()
        specializations = specialization_services.get_all_specializations()
        return render(request, "admin/doctors/doctor_add.html", {"departments": departments, "specializations": specializations})

    def post(self, request):
        print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII", request.POST)
        firstName = request.POST.get("firstName")
        middleName = request.POST.get("middleName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        clinic_address = request.POST.get("clinic_address")
        city = request.POST.get("city")
        pin_code = request.POST.get("pin_code")

        license_number = request.POST.get("licenseNumber")
        license_expiry = request.POST.get("licenseExpiry")

        specialization_id = request.POST.get("specialization")
        department_id = request.POST.get("department")

        degree = request.POST.get("degree")
        institution = request.POST.get("institution")
        completion_year = request.POST.get("completion_year")

        experience = request.POST.get("experience")
        consultation_fee = request.POST.get("consultation_fee")
        bio = request.POST.get("bio")
        dob = request.POST.get("dob")

        profile_picture = request.FILES.get("profile_photo")

        # Create doctor user
        dr_user = user_services.create_doctor_user(
            firstName, middleName, lastName, email
        )
        
        specialization = specialization_services.get_specialization_by_id(specialization_id)

        doctor = doctor_services.doctor_add(
            dr_user=dr_user,
            license_number=license_number,
            license_expiry_date=license_expiry,
            profile_picture=profile_picture,
            consultation_fee=consultation_fee,
            specialization=specialization,
            experience_years=experience,
            bio=bio,
            dob=dob,
            clinic_address=clinic_address,
            city=city,
            pin_code=pin_code,
            contact_number=phone
        )
        qualification_services.add_qualification(
            doctor, degree, institution, completion_year
        )
        

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