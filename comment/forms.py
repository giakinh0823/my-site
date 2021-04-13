from django import forms
from django.forms.fields import MultipleChoiceField
from .models import *
from django.forms import widgets
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple



class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('name', 'email', 'title', 'content') 