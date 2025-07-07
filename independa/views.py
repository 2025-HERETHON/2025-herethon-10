from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from independa.forms import ContractChecklistForm
from independa.models import ChecklistGroup, ContractChecklist, MovingChecklist, RoomCondition, WomenSafetyPreference
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
    room_condition = RoomCondition.objects.create(
        noise=False,
        infrastructure=False,
        safety=False,
        no_leakage=False,
        no_mold=False,
        bathroom_drainage=False,
        windows_doors_work=False,
        wallpaper_flooring=False,
        water_condition=False,
        boiler_condition=False,
        lighting=False,
        basic_options=False
    )

    women_safety = WomenSafetyPreference.objects.create(
        female_only_room=False,
        female_parking=False,
        female_gym=False,
        female_study_cafe=False,
        safe_night_street=False
    )

    # 3. 계약 체크리스트 생성
    ContractChecklist.objects.create(
        checklist_group=checklist_group,
        user=user,
        min_rent_budget=0,
        min_manage_budget=0,
        min_deposit_budget=0,
        owner_verified=False,
        mortgage_verified=False,
        illegal_building_verified=False,
        room_condition=room_condition,
        deposit_insurance=False,
        women_safety_preference=women_safety,
        contract_write=False,
        contract_copy_keep=False,
        deposit_transfer=False,
        cost_receipt_keep=False,
        move_in_report=False,
        receive_move_in_date=False,
        change_address=False,
        transfer_public_utilities=False
    )

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

def contract_checklist_edit_view(request):
    checklist = ContractChecklist.objects.filter(user_id=request.user.id).first()
    
    if not checklist:
        return redirect('independa:create_checklists')

    if request.method == 'POST':
        form = ContractChecklistForm(request.POST, instance=checklist)
        if form.is_valid():
            form.save()
            return redirect('independa:contract_checklist_edit')
    else:
        form = ContractChecklistForm(instance=checklist)

    simple_fields = [
        'contract_write',
        'contract_copy_keep',
        'deposit_transfer',
        'cost_receipt_keep',
        'move_in_report',
        'receive_move_in_date',
        'change_address',
        'transfer_public_utilities',
    ]

    room_condition_fields = [
        'noise', 'infrastructure', 'safety', 'no_leakage', 'no_mold',
        'bathroom_drainage', 'windows_doors_work', 'wallpaper_flooring',
        'water_condition', 'boiler_condition', 'lighting', 'basic_options'
    ]

    women_safety_fields = [
        'female_only_room', 'female_parking', 'female_gym',
        'female_study_cafe', 'safe_night_street'
    ]
    
    independenceplan = IndependencePlan.objects.filter(user_id=request.user.id).first()

    return render(request, 'test_checklist_contract.html', {
        'form': form,
        'room_condition_fields': room_condition_fields,
        'women_safety_fields': women_safety_fields,
        'simple_fields': simple_fields,
        'independenceplan':independenceplan
    })

