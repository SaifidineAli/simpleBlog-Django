from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    edit_article = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Article
        fields = ('title', 'content')
        
        
class DeleteArticleForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    
class CommentForm(forms.ModelForm):
    edit_comment = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Comment
        fields = ('author', 'content')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }