from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.core.utilities.otp_service import send_otp_code, verify_otp_code


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        # Handle registration logic here
        return redirect('home')  # Redirect to home after registration
    
class LoginView(View):
    def get(self, request):
        return render(request, 'enduser/login.html')

    def post(self, request):
        # Handle login logic here
        return redirect('home')  # Redirect to home after login    

def send_otp_view(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        if not contact:
            return JsonResponse({"status": "error", "message": "Contact required"}, status=400)
        
        send_otp_code(contact, purpose="login")  # can be signup, reset_password, etc.
        return JsonResponse({"status": "success", "message": "OTP sent successfully"})

def verify_otp_view(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        otp_code = request.POST.get("otp")

        if not contact or not otp_code:
            return JsonResponse({"status": "error", "message": "Missing fields"}, status=400)

        if verify_otp_code(contact, otp_code, purpose="login"):
            return JsonResponse({"status": "success", "message": "OTP verified"})
        else:
            return JsonResponse({"status": "error", "message": "Invalid or expired OTP"}, status=400)
