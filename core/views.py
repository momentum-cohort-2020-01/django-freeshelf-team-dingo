from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Book, Category, User, Favorite
from .forms import BookForm

@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'core/books.html', {'books': books, 'favorite_books': favorite_books})


def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, "pk": pk})


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        category = request.POST.get('category')
        form.fields['category'].choices = [(category, category)]
        if form.is_valid():
            book = form.save()
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'core/new_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        category = request.POST.get('category')
        form.fields['category'].choices = [(category, category)]
        if form.is_valid():
            book = form.save()
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'core/edit_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('/')


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category = Book.objects.filter(category=category)
    return render(request, 'core/books_by_category.html', {'books': books_for_category, 'category': category})


def get_favorite_books_for_user(request):
    user = User.objects.get(username=request.user.username)
    favorite_books = [favorite.book for favorite in user.favorites.all()]
    return favorite_books