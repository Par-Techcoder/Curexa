from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from apps.core.utilities.decorators import anonymous_required, admin_required

@anonymous_required(redirect_url="/admin/" )
class AdminLoginView(View):    
    def get(self, request):
        
        return render(request, 'admin/auth/admin_login.html')

    def post(self, request):
        # Logic for handling admin login
        # This would typically involve authentication checks
        return redirect('admin_dashboard')
    
@admin_required(login_url="/admin/login/")    
class AdminLogoutView(View):
    def get(self, request):
        logout(request)        
        return redirect('admin_login')