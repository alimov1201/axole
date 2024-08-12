from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    mail = models.EmailField()
    subject = models.CharField(max_length=221)
    message = models.TextField()
