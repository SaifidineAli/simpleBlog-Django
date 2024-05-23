from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    edit_article = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Article
        fields = ('title', 'content')
        
        
class DeleteArticleForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)