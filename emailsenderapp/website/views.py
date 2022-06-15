from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def hello_luisgerardo(request):
    return HttpResponse("Hello, Luis Gerardo")

def hello_maria(request):
    return HttpResponse("Hello, María")

def hello_sombri(request):
    return HttpResponse("Hello, Sombri")

def hello(request, names):
    return HttpResponse(f'Hello, {names}!')

def emails(request):
    return render(request, 'emails.html')

def add_emails(request):
    return render(request, 'add_emails.html')