"""
URL configuration for simpleblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('articles/', blog.views.home, name='article-list'),
    path('articles/new/', blog.views.article_add, name='article-add'),
    path('articles/<int:id>/change/', blog.views.article_edit, name='article-edit'),
    path('articles/<int:id>/delete/', blog.views.article_delete, name='article-delete'),
    path('articles/<int:id>/commentaires/', blog.views.article_commentaires, name='article-commentaires'),
]
