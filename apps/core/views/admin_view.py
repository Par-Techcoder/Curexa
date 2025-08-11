from django.views import View
from django.shortcuts import render, redirect


class AdminDashboardView(View):
    def get(self, request):
        # Logic for rendering the admin dashboard
        return render(request, 'admin/dashboard.html')
