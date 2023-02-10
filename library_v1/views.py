from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    # return HttpResponse("This is the registration page.")
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
