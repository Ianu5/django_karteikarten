from django import forms
from .models import Card, Tag

class TagForm(forms.ModelForm):
    class Meta():
        model = Tag
        fields = ['name', 'users_using_tag']


class CardForm(forms.ModelForm):
    new_tags = forms.CharField(max_length='100', required=False, help_text='Enter new tags separated by commas.')

    class Meta():
        model = Card
        fields = ['foreign_word', 'translation', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    # need to change the save function to incorporate the new tags if some were given


""" possible things after understanding and writing it yourself
    def save(self, commit=True):
        # Save the post first
        post = super().save(commit=False)
        if commit:
            post.save()
        
        # Handle the new tags input
        new_tags = self.cleaned_data.get('new_tags')
        if new_tags:
            tag_names = new_tags.split(',')
            for name in tag_names:
                tag_name = name.strip()
                # Create new tags if they don't exist already
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)  # Add the tag to the post

        return post
"""
