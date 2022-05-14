from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'img')
        labels = {'title':'title', 'content':'content', 'img':'img'}

        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'cols':50, 'placeholder':'まほちだよーーー🐈'}),
            'title': forms.Textarea(attrs={'rows':1, 'cols':50, 'placeholder':'まほち！愛してる！'})
        }