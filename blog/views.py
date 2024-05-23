from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, DeleteArticleForm, CommentForm

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


def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    else:
        form = ArticleForm(instance=article)
        
    return render(request, 'blog/blog_edit.html', context={'form': form})


def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST)
        if form.is_valid():
            article.delete()
            return redirect('article-list')
    else:
        form = DeleteArticleForm()
    
    return render(request, 'blog/article_delete.html', context={'form': form})


def article_commentaires(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            # Réinitialiser le formulaire après soumission
            form = CommentForm()
    else:
        form = CommentForm()
    
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/article_commentaires.html', context=context)