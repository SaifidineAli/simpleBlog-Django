from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    edit_article = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Article
        fields = ('title', 'content')