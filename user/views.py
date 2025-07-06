from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, IndependencePlanForm, LoginForm
from django.http import HttpResponse

def signup_view(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        plan_form = IndependencePlanForm(request.POST)

        if user_form.is_valid() and plan_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # 비밀번호 해시화
            user.save()

            plan = plan_form.save(commit=False)
            plan.user = user
            plan.save()

            login(request, user)  # 회원가입 후 바로 로그인 처리
            return redirect('user:login')  # 로그인 화면으로 이동 (임시)
    else:
        user_form = SignupForm()
        plan_form = IndependencePlanForm()

    return render(request, 'test_signup.html', {
        'user_form': user_form,
        'plan_form': plan_form,
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # 다음 페이지 연결 필요 (현재 임시 상태)
            return HttpResponse(f"로그인 성공! {user.email}")
    else:
        form = LoginForm()

    # login.html 연결
    return render(request, 'test_login.html', {'form': form})