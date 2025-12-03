from django.views import View
from django.shortcuts import render,redirect

class AdminProfileView(View):
    def get(self, request):
        context = {
            "user": request.user,
        }
        return render(request, "admin/profile/profile.html", context)