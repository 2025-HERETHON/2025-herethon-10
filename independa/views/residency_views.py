from django.conf import settings
from django.shortcuts import render

from independa.models import CheckAll
from user.models import IndependencePlan


def residency_checklist_edit_view(request):
    check=CheckAll.objects.get(user_id=request.user.id)
    independenceplan = IndependencePlan.objects.filter(user_id=request.user.id).first()
    myjskey=settings.MYJSKEY
    
    context = {
        # 'form': form,
        'check':check,
        'independenceplan':independenceplan,
        'myjskey':myjskey,
    }
    return render(request, 'test_checklist_residency.html', context )