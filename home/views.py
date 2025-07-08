# home/views.py
from django.shortcuts import redirect, render

def root_redirect(request):
    # 루트 경로 (/)에 접속하면 로그인 화면으로 이동
    return redirect('/user/login/')  # 또는 redirect('user:login') if 네임스페이스 쓴다면

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/user/login/')  # 로그인 안 된 사람도 로그인 화면으로 이동
    return render(request, 'test_home.html', {
        'user': request.user,
    })
