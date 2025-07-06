from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('test_signup/', views.signup_view, name='test_signup'),
    path('test_login/', views.login_view, name='test_login'),
]

