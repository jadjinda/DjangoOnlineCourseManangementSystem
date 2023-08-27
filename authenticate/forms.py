from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

#class SignupForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = get_user_model()
#        fields = ('username', 'email', 'password')

