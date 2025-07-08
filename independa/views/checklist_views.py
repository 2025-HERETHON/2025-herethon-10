from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from independa.forms import ContractChecklistForm
from independa.models import ChecklistGroup, ContractChecklist, MovingChecklist, RoomCondition, WomenSafetyPreference
from independa.views.contract_views import contract_checklists
from user.models import IndependencePlan

@login_required
def inde_home_view(request):
    return render(request, 'test_inde_home.html')

@login_required
def create_checklists_view(request):
    user = request.user
    
    if ChecklistGroup.objects.filter(user_id=request.user.id).exists() :
        return redirect('independa:contract_checklist_edit')

    # 1. 그룹 생성
    checklist_group = ChecklistGroup.objects.create(
        user=user
    )

    # 2. ContractChecklist 관련 서브모델 생성
    contract_checklists(user, checklist_group)

    # 4. 입주 체크리스트 생성 (기본값으로)
    MovingChecklist.objects.create(
        checklist_group=checklist_group,
        user=user
    )

    # 5. 이사 체크리스트 생성 (기본값으로)
    MovingChecklist.objects.create(
        checklist_group=checklist_group,
        user=user
    )

    return redirect('independa:contract_checklist_edit')

