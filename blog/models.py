from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='media')
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
