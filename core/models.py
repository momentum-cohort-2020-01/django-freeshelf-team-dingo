from django.contrib.auth.models import User 
from django.db import models
from django.utils.text import slugify

Categories = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JavaScript', 'JavaScript'),
    ('JSON', 'JSON'),
    ('AJAX', 'AJAX'),
    ('Python', 'Python'),
    ('Django', 'Django')
)


class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING, null=True, blank=True)
    

    def __str__(self):
        return f'Book title: {self.title} Author: {self.author} Description: {self.description} URL: {self.url} Category: {self.category}'

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=100, choices=Categories)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

# class User(AbstractUser)

class Favorite(models.Model):
    my_favorite = models.ForiegnKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'my_favorite: {self.my_favorite}, Book: {self.book}'

