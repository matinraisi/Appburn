from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class SplashView(View):
    template_name = 'splash/splashScreen.html'
    def get(self , request):
        return render(request , self.template_name)

class SplashStartView(View):
    template_name = 'splash/onborading.html'
    def get(self , request):
        return render(request , self.template_name)