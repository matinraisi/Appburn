from django.urls import path 
from .views import *

urlpatterns = [
    path('' , SplashView.as_view()),
    path('start/' , SplashStartView.as_view())


]
