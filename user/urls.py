from django.urls import path
from . import views
from .views import login_view

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', login_view, name='login'),
]
