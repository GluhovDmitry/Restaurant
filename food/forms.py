from django import forms


class Form(forms.Form):
    address = forms.CharField()