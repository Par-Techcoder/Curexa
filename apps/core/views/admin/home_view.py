from django.views import View
from django.shortcuts import render, redirect
from apps.core.utilities.decorators import admin_required


@admin_required(login_url="/admin/login/")
class AdminDashboardView(View):
    def get(self, request):
        context = {
        "user": request.user,
        }
        return render(request, "admin/dashboard/dasboard.html", context)