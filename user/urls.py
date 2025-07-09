from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('api/get_sido/', views.get_sido, name='get_sido'),
    path('api/get_sigungu/', views.get_sigungu, name='get_sigungu'),
]

