"""
Definition of forms.
"""

from django import forms
from django.core.validators import validate_email

from .models import Users

class UserForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = Users
		fields = ['name','email']
		
	def clean_email(self):
		email = self.cleaned_data['email']
		if Users.objects.filter(email=email).exists():
			raise forms.ValidationError('Email already exists')
		return email