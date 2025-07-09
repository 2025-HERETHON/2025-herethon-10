from django.conf import settings
from django.shortcuts import redirect, render

from independa.forms import ResidencyChecklistForm
from independa.models import CheckAll, ResidencyChecklist
from user.models import IndependencePlan

def residency_checklists(user, checklist_group):
    ResidencyChecklist.objects.create(
        user=user,
        checklist_group=checklist_group,

        check_utilities=False,
        check_heating=False,
        set_doorlock_password=False,
        
        check_fire_detector=False,
        check_window_locks=False,
        locate_circuit_breaker=False,
        
        check_recycling_days=False,
        setup_wifi_appliances=False,
        prepare_emergency_kit=False,
        
        prepare_laundry_detergent=False,
        prepare_kitchen_supplies=False,
        prepare_toiletries=False,
        prepare_garbage_bags=False,
        prepare_drinking_water=False,
    )

def is_residency_checklist_complete(checklist):
    # simple_fields 체크
    required_fields = [
        # 기본 점검
        'check_utilities',
        'check_heating',
        'set_doorlock_password',

        # 안전·보안 점검
        'check_fire_detector',
        'check_window_locks',
        'locate_circuit_breaker',

        # 생활 정착
        'check_recycling_days',
        'setup_wifi_appliances',
        'prepare_emergency_kit',

        # 생활 필수품 보충하기
        'prepare_laundry_detergent',
        'prepare_kitchen_supplies',
        'prepare_toiletries',
        'prepare_garbage_bags',
        'prepare_drinking_water',
    ]
    
    # 모든 필드가 True인지 확인
    for field in required_fields:
        value = getattr(checklist, field, False)
        print(f"{field}: {value}")  # 디버깅용
        if not value:
            return False
    return True


def residency_checklist_edit_view(request):
    check=CheckAll.objects.get(user_id=request.user.id)
    independenceplan = IndependencePlan.objects.filter(user_id=request.user.id).first()
    checklist = ResidencyChecklist.objects.filter(user_id=request.user.id).first()
    
    if not checklist:
        return redirect('independa:create_checklists')
    
    if request.method == 'POST':
        form = ResidencyChecklistForm(request.POST, instance=checklist)

        if form.is_valid():
            checklist_form = form.save(commit=False)
            checklist_form.user = request.user
            checklist_form.save()
            
            check=CheckAll.objects.get(user_id=request.user.id)
            check_all=is_residency_checklist_complete(checklist)
            check.residency_all=check_all
            check.save()
            print("체크올 : ", check_all)
            
            return redirect('independa:residency_checklist_edit')
    else:
        form = ResidencyChecklistForm(instance=checklist)
    
    check=CheckAll.objects.get(user_id=request.user.id)
    myjskey=settings.MYJSKEY
    
    context = {
        'form': form,
        'check':check,
        'independenceplan':independenceplan,
        'myjskey':myjskey,
    }
    return render(request, 'test_checklist_residency.html', context )