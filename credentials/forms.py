from django import forms

class InputForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Email = forms.CharField(max_length=200)
    Address = forms.CharField(max_length=200)