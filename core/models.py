from django.db import models

Categories = (
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('javascript', 'JavaScript'),
    ('json', 'JSON'),
    ('ajax', 'AJAX'),
    ('python', 'Python'),
    ('django', 'Django')
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
