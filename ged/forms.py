from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Directory, Document


class ConnexionForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'parent']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']