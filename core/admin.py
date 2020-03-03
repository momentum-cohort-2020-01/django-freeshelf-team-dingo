from django.contrib import admin

from .models import Book, Category, Priority

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Priority)

# Register your models here.
