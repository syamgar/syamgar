from django.shortcuts import render
from django.http import HttpResponse

def stream(request):
    return render(request, 'stream.html')

