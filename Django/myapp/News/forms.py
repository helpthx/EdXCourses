from django import forms


class registroform(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)
	email = forms.CharField(max_length=100)
	telefone = forms.CharField(max_length=100)