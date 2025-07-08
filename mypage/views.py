from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import IndependencePlan
from .forms import UserUpdateForm, IndependencePlanUpdateForm


@login_required
def profile_edit(request):
    user = request.user
    plan = get_object_or_404(IndependencePlan, user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        plan_form = IndependencePlanUpdateForm(request.POST, instance=plan)

        if user_form.is_valid() and plan_form.is_valid():
            user_form.save()
            plan_form.save()
            return redirect('mypage:profile_edit')
    else:
        user_form = UserUpdateForm(instance=user)
        plan_form = IndependencePlanUpdateForm(instance=plan)

    return render(request, 'user_update.html', {
        'user_form': user_form,
        'plan_form': plan_form,
    })
