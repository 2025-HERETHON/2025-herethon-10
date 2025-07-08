from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from independa.forms import ContractChecklistForm
from independa.models import CheckAll, ChecklistGroup, ContractChecklist, MovingChecklist, RoomCondition, WomenSafetyPreference
from user.models import IndependencePlan

#체크리스트 초기값으로 생성하는 함수
def contract_checklists(user, checklist_group):
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

#체크리스트 모두 체크되어 있나 확인
def is_contract_checklist_complete(checklist):
    # simple_fields 체크
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
    
    # 등기부등본 체크
    register_fields =[
        'owner_verified',
        'mortgage_verified',
        'illegal_building_verified',
    ]
    

    # deposit_insurance 단일 필드 체크
    required_fields = simple_fields + register_fields + ['deposit_insurance']

    # 모든 필드가 True인지 확인
    for field in required_fields:
        value = getattr(checklist, field, False)
        print(f"{field}: {value}")  # 디버깅용
        if not value:
            return False
    return True

def contract_checklist_edit_view(request):
    checklist = ContractChecklist.objects.filter(user_id=request.user.id).first()
    independenceplan = IndependencePlan.objects.filter(user_id=request.user.id).first()
    
    if not checklist:
        return redirect('independa:create_checklists')

    if request.method == 'POST':
        form = ContractChecklistForm(request.POST, instance=checklist)

        if form.is_valid():
            form.save()
            area_si = request.POST.get('area_si', '').strip()
            area_sgg = request.POST.get('area_sgg', '').strip()

            if area_si:
                independenceplan.area_si = area_si
            if area_sgg:
                independenceplan.area_sgg = area_sgg
            
            independenceplan.save()
            
            check=CheckAll.objects.get(user_id=request.user.id)
            check_all=is_contract_checklist_complete(checklist)
            check.contract_all=check_all
            check.save()
            print("체크올 : ", check_all)
            
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
    
    check=CheckAll.objects.get(user_id=request.user.id)

    context = {
        'form': form,
        'room_condition_fields': room_condition_fields,
        'women_safety_fields': women_safety_fields,
        'simple_fields': simple_fields,
        'independenceplan':independenceplan,
        'check':check,
    }

    return render(request, 'test_checklist_contract.html', context)

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
            
        except ContractChecklist.DoesNotExist:
            print("삭제할 ContractChecklist 없음")

        contract_checklists(user, checklist_group)

    else:
        print(f"'{categ}'는 일치하지 않음")

    return redirect('independa:contract_checklist_edit')
