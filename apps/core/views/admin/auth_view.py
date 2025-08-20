from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout


class AdminLoginView(View):
    def get(self, request):
        # Logic for rendering the admin login page
        return render(request, 'admin/auth/admin_login.html')

    def post(self, request):
        # Logic for handling admin login
        # This would typically involve authentication checks
        return redirect('admin_dashboard')
    
class AdminLogoutView(View):
    def get(self, request):
        logout(request)        
        return redirect('admin_login')