from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect), 
    path('home/', views.home_view, name='home'),
]
