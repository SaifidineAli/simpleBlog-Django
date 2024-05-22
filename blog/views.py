from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def home(request):
    articles = Article.objects.all()
    
    return render(request, 'blog/blog_list.html', context={'articles': articles})


def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    else:
        form = ArticleForm()
    
    return render(request, 'blog/blog_add.html', context={'form': form})