# home/views.py
from django.shortcuts import redirect, render

def root_redirect(request):
    return redirect('/accounts/login/')

def home_view(request):
    plan = None
    if request.user.is_authenticated:
        # 사용자 독립 계획 정보 로드 (필요한 경우)
        from user.models import IndependencePlan
        plan = IndependencePlan.objects.filter(user=request.user).first()

    return render(request, 'home.html', {
        'user': request.user,
        'plan': plan
    })

