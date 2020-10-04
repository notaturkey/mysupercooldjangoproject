from django import forms

class UserForm(forms.Form):
    email = forms.CharField(label='inputEmail', max_length=100)
    username = forms.CharField(label='inputUser', max_length=100)
    password = forms.CharField(label='inputPass', max_length=100)
    confPassword = forms.CharField(label='inputPass2', max_length=100)