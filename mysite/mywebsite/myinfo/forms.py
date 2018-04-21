from django import forms

from .models import Data


class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = ('name', 'comment_about_me','Email','address')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'comment_about_me': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
