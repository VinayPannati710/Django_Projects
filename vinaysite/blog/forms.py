from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    model=Post
    class Meta():
        fields=('text','title','author')
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
class CommentForm(forms.ModelForm):
    model=Comment
    class Meta():
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})
        }