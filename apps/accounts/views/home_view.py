from django.views import View
from django.shortcuts import render,redirect

class HomeView(View):
    def get(self, request):
        return render(request, 'enduser/home.html')

    def post(self, request):

        return
