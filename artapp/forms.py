from django import forms
from .models import BlogPost,Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image' ,'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select a category'
        self.initial['category'] = '' 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']