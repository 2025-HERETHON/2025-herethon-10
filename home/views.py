from django.shortcuts import render, redirect

def landing_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # 로그인 돼 있으면 홈으로
    return render(request, 'home/landing.html')  # 아니면 랜딩 페이지 보여줌

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('landing')  # 로그인 안 돼 있으면 랜딩으로
    return render(request, 'home/home.html', {
        'user': request.user,
    })
