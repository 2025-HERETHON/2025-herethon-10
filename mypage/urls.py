from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('mypage/', views.profile_edit, name='mypage'),  # 회원정보 수정
]
