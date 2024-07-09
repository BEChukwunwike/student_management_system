from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'is_student', 'is_admin', 'is_lecturer')

    def clean(self):
        cleaned_data = super().clean()
        if sum([cleaned_data.get('is_student'), cleaned_data.get('is_admin'), cleaned_data.get('is_lecturer')]) > 1:
            raise forms.ValidationError("A user can only be a student, admin, or lecturer, not more than one.")
        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_student', 'is_admin', 'is_lecturer')

    def clean(self):
        cleaned_data = super().clean()
        if sum([cleaned_data.get('is_student'), cleaned_data.get('is_admin'), cleaned_data.get('is_lecturer')]) > 1:
            raise forms.ValidationError("A user can only be a student, admin, or lecturer, not more than one.")
        return cleaned_data
