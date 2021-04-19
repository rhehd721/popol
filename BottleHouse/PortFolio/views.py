from django.shortcuts import render

def enter(request):
    return render(request, './enter.html')

def home(request):
    return render(request, './home.html')