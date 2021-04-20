from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PortFolio

from pathlib import Path, os

BASE_DIR = Path(__file__).resolve().parent.parent


def enter(request):
    return render(request, './enter.html')

def home(request):
    modle = PortFolio.objects.all()
    return render(request, './home.html', {'modle' : modle, 'BASE_DIR' : BASE_DIR})

def introduce(request):
    return render(request, './introduce.html')

def accept(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        password = request.POST.get('Password', '')
        username = request.POST.get('Id', '')

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('home')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, './enter.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, './enter.html')


def guest(request):
    if request.method == 'POST':
        return redirect('home')