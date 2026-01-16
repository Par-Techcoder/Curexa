from django.views import View
from django.shortcuts import render, redirect

class SalesReportsView(View):
    def get(self, request):
        # Logic to gather report data can be added here
        return render(request, 'admin/reports/sales_report.html')

class InventoryReportsView(View):
    def get(self, request):
        # Logic to gather report data can be added here
        return render(request, 'admin/reports/inventory_report.html')
    
class AppointmentReportsView(View):
    def get(self, request):
        # Logic to gather report data can be added here
        return render(request, 'admin/reports/appointment_report.html')
