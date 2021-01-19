
from django import forms
from django.forms import fields, widgets
from froala_editor.widgets import FroalaEditor
from . models import PageForm

class PageForm(forms.ModelForm):
    name = forms.CharField(max_length=560, label='',required=True)
    email = forms.EmailField(label='', required=True)
    content = forms.CharField(widget=FroalaEditor, label='',required=True)
    class Meta:
        model = PageForm
        fields = ('name','email', 'content')