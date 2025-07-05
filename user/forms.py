from django import forms
from .models import User, IndependencePlan
from django.contrib.auth.forms import AuthenticationForm

ROOMATE_CHOICES = [
    ('동거인 없음', '동거인 없음'),
    ('동거인 있음', '동거인 있음'),
]

MOVE_DATE_CHOICES = [
    ('2025-07', '2025년 7월'),
    ('2025-08', '2025년 8월'),
    ('2025-09', '2025년 9월'),
]


# 기본 정보 입력 폼
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    GENDER_CHOICES = [
        ('여성', '여성'),
        ('남성', '남성'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'gender', 'birth_date', 'job']

# 독립계획 정보 입력 폼
class IndependencePlanForm(forms.ModelForm):
    move_date = forms.ChoiceField(choices=MOVE_DATE_CHOICES)
    has_roomate = forms.ChoiceField(choices=ROOMATE_CHOICES, widget=forms.RadioSelect)

    # ⚠️ area_sgg(시/군/구)는 area_si(시/도)에 따라 동적으로 변경될 예정
    
    class Meta:
        model = IndependencePlan
        exclude = ['user']
        
# 로그인 폼
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="이메일",
        widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력하세요'})
    )
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력하세요'})
    )