from django.contrib import admin

from .models import Book, Category, Favorite

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)

# Register your models here.
