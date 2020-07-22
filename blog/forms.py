from django import forms
from .models import Comment, ContactMe, RegisterUser

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'comment',
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = [
            'name',
            'email',
            'message',
        ]

class registerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type':'password',
    }))
    class Meta:
        model=RegisterUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]