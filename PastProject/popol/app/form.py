
from django import forms
from .models import Popol

# model을 기반으로 폼을 만들고 싶을때 작성


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ( 'content',)
