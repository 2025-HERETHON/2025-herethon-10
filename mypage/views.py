from django.shortcuts import render, redirect
from user.models import User, IndependencePlan
from .forms import UserUpdateForm, IndependencePlanUpdateForm

def profile_edit(request):
    user = request.user
    plan = IndependencePlan.objects.filter(user=user).order_by('-id').first()

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        plan_form = IndependencePlanUpdateForm(request.POST, instance=plan)

        if user_form.is_valid() and plan_form.is_valid():
            user_form.save()
            plan = plan_form.save(commit=False)

        # 지역 정보 수동 반영
            area_si = request.POST.get('area_si', '').strip()
            area_sgg = request.POST.get('area_sgg', '').strip()
            if area_si:
                plan.area_si = area_si
            if area_sgg:
                plan.area_sgg = area_sgg

            plan.save()
            return redirect('mypage:profile_edit')

    else:
        user_form = UserUpdateForm(instance=user)
        plan_form = IndependencePlanUpdateForm(instance=plan)

    return render(request, 'test_user_update.html', {
        'user_form': user_form,
        'plan_form': plan_form,
    })
