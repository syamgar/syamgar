from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
#    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def tLogin(request):
    return render(request, 'teach_login.html')

def sLogin(request):
    return render(request, 'stud_login.html')

def report(request):
    return render(request, 'visual.html')