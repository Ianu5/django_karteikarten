from django import forms
from .models import Card, Tag

class TagForm(forms.ModelForm):
    class Meta():
        model = Tag
        fields = ['name']


class CardForm(forms.ModelForm):
    class Meta():
        model = Card
        fields = ['foreign_word', 'translation', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
