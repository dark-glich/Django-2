from django import forms

from .models import comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = [
            'comment',
            'name',
            'email'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'comment-name'}),
            'email': forms.TextInput(attrs={'class': 'comment-email'}),
            'comment': forms.Textarea(attrs={'class': 'comment', 'placeholder': 'Enter Your Comment'}),
        }

