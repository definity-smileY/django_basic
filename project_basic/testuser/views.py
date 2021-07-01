from django.http import HttpResponse
from django.shortcuts import render, redirect
# 암호화 모듈
from django.contrib.auth.hashers import make_password, check_password
from .models import testuser
# Create your views here.

def home(request):
    return HttpResponse('HOME')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None) 

        res_date = {}
        if not (username and password):
            res_date['error'] = '모든 값을 입력해야합니다.'
        else:
            test_uesr = testuser.objects.get(username=username)
            if check_password(password, test_uesr.password):
                # request.session['user'] = testuser.id
                # return redirect('/')
                pass
            else:
                res_date['error'] = '비밀번호가 틀렸습니다.'

        return render(request, 'login.html', res_date)


def register(request):
    if request.method == 'GET':        
        return render(request, 'register.html')
    elif request.method == 'POST':
        useremail = request.POST.get('useremail', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_error = {}

        if not (useremail and username and password and re_password):
            res_error['error'] = '모든 값을 입력해야합니다.'            
        elif password != re_password:
            res_error['error'] = '비밀번호가 다릅니다.'
        else:
            test_user = testuser(
                useremail=useremail,
                username=username,
                
                # 암호화
                password=make_password(password),
                
            )

            test_user.save()

        return render(request, 'register.html', res_error)