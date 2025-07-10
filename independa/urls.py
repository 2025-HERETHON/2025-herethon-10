from django.urls import path
from independa.views.contract_views import contract_checklist_edit_view
from independa.views.checklist_views import inde_home_view, create_checklists_view, reset_checklist_view
from independa.views.moving_veiws import moving_checklist_edit_view
from independa.views.residency_views import residency_checklist_edit_view
from independa.views.local_infra_views import local_infra_view, save_place, category_search_map, keyword_search_map
from independa.views.scrap_infra_views import scrap_infra_view, delete_place_view, filter_saved_places_view


app_name='independa'

urlpatterns = [
    path('inde_home/', inde_home_view, name="inde_home"),
    path('create_checklists/', create_checklists_view, name="create_checklists"),
    path('reset_checklist/<str:categ>/', reset_checklist_view, name="reset_checklist"),
    
    path('contract_checklist_edit/', contract_checklist_edit_view, name="contract_checklist_edit"),
    path('moving_checklist_edit/', moving_checklist_edit_view, name="moving_checklist_edit"),
    path('residency_checklist_edit/', residency_checklist_edit_view, name="residency_checklist_edit"),
    
    path('local_infra/', local_infra_view, name="local_infra"),
    # path('category_search/<str:category_group_code>/', category_search_map, name='category_search'),
    
    # path("save_place/", save_place, name="save_place"),
    path('category_search/<str:category_group_code>/', category_search_map, name='category_search'),
    path('save_place/', save_place, name='save_place'),
    path('keyword_search/', keyword_search_map, name='keyword_search'),
    
    path('scrap_infra/', scrap_infra_view, name="scrap_infra"),
    path('delete_place/<str:place_id>/', delete_place_view, name='delete_place'),
    path('filter_saved_places/', filter_saved_places_view, name='filter_saved_places'),
    
    
]
