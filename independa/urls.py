from django.urls import path
from independa.views.contract_views import contract_checklist_edit_view, reset_checklist_view
from independa.views.checklist_views import inde_home_view, create_checklists_view

app_name='independa'

urlpatterns = [
    path('inde_home/', inde_home_view, name="inde_home"),
    path('create_checklists/', create_checklists_view, name="create_checklists"),
    path('contract_checklist_edit/', contract_checklist_edit_view, name="contract_checklist_edit"),
    path('reset_checklist/<str:categ>/', reset_checklist_view, name="reset_checklist"),
]
