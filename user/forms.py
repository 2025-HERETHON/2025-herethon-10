from django import forms
from .models import User, IndependencePlan
from django.contrib.auth.forms import AuthenticationForm

# 기본 정보 입력 폼
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'gender', 'birth_date', 'job']

# 독립계획 정보 입력 폼
class IndependencePlanForm(forms.ModelForm):
    class Meta:
        model = IndependencePlan
        exclude = ['user']  # 유저는 view에서 할당
