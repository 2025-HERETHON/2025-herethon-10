from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm, IndependencePlanForm

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
            return redirect('home:home')  # 홈 화면으로 리디렉트 (URL name에 따라 수정 가능)
    else:
        user_form = SignupForm()
        plan_form = IndependencePlanForm()

    return render(request, 'user/signup.html', {
        'user_form': user_form,
        'plan_form': plan_form,
    })
