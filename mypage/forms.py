from django import forms
from user.models import User, IndependencePlan

MOVE_DATE_CHOICES = [
    ('2025-07', '2025년 7월'),
    ('2025-08', '2025년 8월'),
    ('2025-09', '2025년 9월'),
]

class UserUpdateForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    
    GENDER_CHOICES = [
        ('여성', '여성'),
        ('남성', '남성'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = User
        fields = ['name', 'email', 'gender', 'birth_date', 'job', 'profile_image']


class IndependencePlanUpdateForm(forms.ModelForm):
    # 숨김 필드 + 필수 아님 (JS로 채움)
    area_si = forms.CharField(widget=forms.HiddenInput())
    area_sgg = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = IndependencePlan
        exclude = ['user']
