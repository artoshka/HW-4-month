from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пороль', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Поворите пороль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError('Пороли не похожи!')
        return cd['password_2']