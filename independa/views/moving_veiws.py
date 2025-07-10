from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from independa.forms import MovingChecklistForm
from independa.models import CheckAll, ChecklistGroup, MovingChecklist
from user.models import IndependencePlan

def moving_checklists(user, checklist_group):
    MovingChecklist.objects.create(
        user=user,
        checklist_group=checklist_group,

        # 이사 하루 전
        unplug_appliances=False,
        keep_valuables_separately=False,
        check_new_home_password=False,
        confirm_moving_time=False,
        finish_trash_sorting=False,

        # 이사 당일
        check_truck_arrival_time=False,
        take_photos_of_old_home=False,

        # 새 집 점검하기
        check_leaks=False,
        check_power_outlets=False,
        check_water_supply=False,

        # 설치 기사 방문 체크하기
        check_appliance_installer=False,
        check_internet_installer=False,

        # 이사 후
        complete_address_registration=False,
        change_address=False,
        check_deposit_settlement=False,
        check_trash_disposal_rules=False,
        check_residence_insurance=False,
    )

#체크리스트 모두 체크되어 있나 확인
def is_moving_checklist_complete(checklist):
    # simple_fields 체크
    required_fields = [
        'unplug_appliances',
        'keep_valuables_separately',
        'check_new_home_password',
        'confirm_moving_time',
        'finish_trash_sorting',
        'check_truck_arrival_time',
        'take_photos_of_old_home',
        'check_leaks',
        'check_power_outlets',
        'check_water_supply',
        'check_appliance_installer',
        'check_internet_installer',
        'complete_address_registration',
        'change_address',
        'check_deposit_settlement',
        'check_trash_disposal_rules',
        'check_residence_insurance'
    ]
    
    # 모든 필드가 True인지 확인
    for field in required_fields:
        value = getattr(checklist, field, False)
        print(f"{field}: {value}")  # 디버깅용
        if not value:
            return False
    return True



def moving_checklist_edit_view(request):
    checklist = MovingChecklist.objects.filter(user_id=request.user.id).first()
    independenceplan = IndependencePlan.objects.filter(user_id=request.user.id).first()
    
    if not checklist:
        return redirect('independa:create_checklists')
    
    if request.method == 'POST':
        form = MovingChecklistForm(request.POST, instance=checklist)

        if form.is_valid():
            checklist_form = form.save(commit=False)
            checklist_form.user = request.user
            checklist_form.save()
            
            check=CheckAll.objects.get(user_id=request.user.id)
            check_all=is_moving_checklist_complete(checklist)
            check.moving_all=check_all
            check.save()
            print("체크올 : ", check_all)
            
            return redirect('independa:moving_checklist_edit')
    else:
        form = MovingChecklistForm(instance=checklist)
        
    
    check=CheckAll.objects.get(user_id=request.user.id)
    myjskey=settings.MYJSKEY
    
    context = {
        'form': form,
        'check':check,
        'independenceplan':independenceplan,
        'myjskey':myjskey,
    }
    return render(request, 'test_checklist_move.html', context )
