from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('edit/', views.profile_edit, name='profile_edit'),  # 회원정보 수정
]
