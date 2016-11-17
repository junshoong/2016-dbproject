from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ('author', 'message')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
