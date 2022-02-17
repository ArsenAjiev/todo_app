from django import forms
from .models import Note
from project.services import slugify


class NoteForm(forms.ModelForm):

    def save(self, commit: bool = True):
        if not self.cleaned_data['slug'] and self.instance:
            self.instance.slug = slugify(self.cleaned_data['title'])
        return super().save(commit=commit)

    class Meta:
        model = Note
        fields = ['title', 'slug', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
