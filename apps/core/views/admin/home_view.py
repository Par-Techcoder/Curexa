from django.views import View
from django.shortcuts import render, redirect
from apps.core.utilities.decorators import admin_required



@admin_required(login_url="/admin/login/")
class AdminDashboardView(View):
    def get(self, request):
        user = request.user
        print(user)
        context = {
        "user": request.user,
        }
        print(context["user"])
        return render(request, 'admin/base.html', context)

