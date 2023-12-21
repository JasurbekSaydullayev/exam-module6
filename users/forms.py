from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginUsersForm(AuthenticationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Parol',
                               widget=forms.PasswordInput(attrs={'class': "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUsersForm(UserCreationForm):
    username = forms.CharField(label="Foydalanuvchi nomini kiriting",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class': "form-input"}))
    password2 = forms.CharField(label="Parolni tasdiqlash", widget=forms.PasswordInput(attrs={'class': "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {'last_name': 'Familiyangizni kiriting',
                  'email': 'E-mail',
                  'first_name': 'Ismingizni kiriting'}
        widgets = {'last_name': forms.TextInput(attrs={'class': 'form-input'}),
                   'email': forms.TextInput(attrs={'class': 'form-input'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-input'})}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Parollar bir-biriga mos kelamdi")
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email bilan oldin ro'yhatdan o'tilgan")
        return email
