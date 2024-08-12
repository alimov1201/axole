from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField()
    author = models.CharField(max_length=221)
    image = models.ImageField(upload_to="article_images/")
    date = models.DateTimeField(auto_now_add=True)


class Email(models.Model):
    mail = models.EmailField()
