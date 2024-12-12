from django import forms
from .models import Card, Tag


class CardForm(forms.ModelForm):
    class Meta():
        model = Card
        fields = ['foreign_word', 'translation']
