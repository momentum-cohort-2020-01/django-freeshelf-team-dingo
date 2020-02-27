from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    # url = #parking lot

# def __str__(self):
#         return f"Note title: {self.title} body: {self.body}"

# Create your models here.
