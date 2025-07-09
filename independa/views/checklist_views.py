from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from independa.forms import ContractChecklistForm
from independa.models import ChecklistGroup, ContractChecklist, MovingChecklist, RoomCondition, WomenSafetyPreference, CheckAll, ResidencyChecklist
from independa.views.contract_views import contract_checklists
from independa.views.residency_views import is_residency_checklist_complete, residency_checklists
from user.models import IndependencePlan
from independa.views.moving_veiws import moving_checklists

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
    moving_checklists(user, checklist_group)

    # 5. 이사 체크리스트 생성 (기본값으로)
    residency_checklists(user, checklist_group)
    
    #6. 체크 진행도
    CheckAll.objects.create(
        checklist_group=checklist_group,
        user=user
    )

    return redirect('independa:contract_checklist_edit')

@require_POST
def reset_checklist_view(request, categ):

    user = request.user

    try:
        checklist_group = ChecklistGroup.objects.get(user=user)
    except ChecklistGroup.DoesNotExist:
        print("ChecklistGroup 없음")
        return redirect('independa:contract_checklist_edit')

    if categ == "contract":
        try:
            checklist = ContractChecklist.objects.get(user=user)
            if checklist.room_condition_id:
                checklist.room_condition.delete()

            if checklist.women_safety_preference_id:
                checklist.women_safety_preference.delete()

            checklist.delete()
            
            check=CheckAll.objects.get(user_id=request.user.id)
            check.contract_all=0
            check.save()
            
        except ContractChecklist.DoesNotExist:
            print("삭제할 ContractChecklist 없음")

        contract_checklists(user, checklist_group)
        
        return redirect('independa:contract_checklist_edit')

    elif categ == "moving":
        try:
            checklist = MovingChecklist.objects.get(user=user)
            checklist.delete()
            check=CheckAll.objects.get(user_id=request.user.id)
            check.moving_all=0
            check.save()
            
        except MovingChecklist.DoesNotExist:
            print("삭제할 MovingChecklist 없음")

        moving_checklists(user, checklist_group)
        
        return redirect('independa:moving_checklist_edit')
        
    elif categ == "residency":
        try:
            checklist = ResidencyChecklist.objects.get(user=user)
            checklist.delete()
            check=CheckAll.objects.get(user_id=request.user.id)
            check.residency_all=0
            check.save()
            
        except ResidencyChecklist.DoesNotExist:
            print("삭제할 ResidencyChecklist 없음")

        residency_checklists(user, checklist_group)
        
        return redirect('independa:residency_checklist_edit')
    
    else:
        print(f"'{categ}'는 일치하지 않음")

    