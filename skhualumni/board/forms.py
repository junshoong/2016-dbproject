from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo',)


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
