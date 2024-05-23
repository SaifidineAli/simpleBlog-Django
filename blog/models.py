from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    #author = models.ForeignKey(User) # Comme on a pas encore fait de gestion des utilisateurs, on n'utilise pas de relation Foreignkey
    author = models.CharField(max_length=50)
    content = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
    