from django.shortcuts import render

from independa.models import CheckAll
from user.models import IndependencePlan


def moving_checklist_edit_view(request):
    check=CheckAll.objects.get(user_id=request.user.id)
    independenceplan = IndependencePlan.objects.filter(user_id=request.user.id).first()
    
    context = {
        # 'form': form,
        'check':check,
        'independenceplan':independenceplan,
    }
    return render(request, 'test_checklist_move.html', context )