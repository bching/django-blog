from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    '''
    Other fields s.a. author is the person currently
    logged in and created_date is automatically set 
    when we create a post
    '''
    class Meta: 
        model = Post
        fields = ('title', 'text',)
