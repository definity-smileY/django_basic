from django.http import HttpResponse
from django.shortcuts import render, redirect
# 암호화 모듈
from django.contrib.auth.hashers import make_password, check_password
from .models import testuser
from .forms import LoginForm

def home(request):
    user_id = request.session.get('user')
    
    if user_id:
        test_user = testuser.objects.get(pk=user_id)
        return HttpResponse(test_user.username)

    return HttpResponse('HOME!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


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