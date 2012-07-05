from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=128, label="Username")
	password = forms.CharField(widget=forms.PasswordInput, label="Password")

class RegistrationForm(LoginForm):
	email = forms.EmailField(label="Email")
	tel	= forms.CharField(label="Telephone")
