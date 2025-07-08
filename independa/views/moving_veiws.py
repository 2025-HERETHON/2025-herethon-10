from django.shortcuts import render

from independa.models import CheckAll


def moving_checklist_edit_view(request):
    check=CheckAll.objects.get(user_id=request.user.id)
    return render(request, 'test_checklist_move.html',{
        # 'form': form,
        'check':check
    } )