from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name  = forms.CharField(max_length=20)
    username   = forms.CharField(label="Username", max_length=10)
    email      = forms.EmailField(label="Email", required=True)
    password   = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput, required=True)
    


class LoginForm(forms.Form):
    username   = forms.CharField(label="Username", max_length=10)
    password   = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput, required=True)
    
