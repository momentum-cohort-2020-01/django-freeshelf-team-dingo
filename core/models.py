from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book title: {self.title} Author: {self.author} Description: {self.description} URL: {self.url}'


