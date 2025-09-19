from django.views import View
from django.shortcuts import render, redirect

class AppointmentListView(View):
    def get(self, request):
        return render(request, "admin/appoinments/todays_appoinments.html")
    
    
class AppointmentAddView(View):
    def get(self, request):
        return render(request, "admin/appoinments/appoinment_book.html") 
    
class AppointmentHistoryView(View):
    def get(self, request):
        return render(request, "admin/appoinments/weekly_schedule.html")       