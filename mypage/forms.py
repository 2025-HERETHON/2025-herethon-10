from django import forms
from user.models import User, IndependencePlan


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'gender', 'birth_date', 'job']


class IndependencePlanUpdateForm(forms.ModelForm):
    class Meta:
        model = IndependencePlan
        exclude = ['user']
