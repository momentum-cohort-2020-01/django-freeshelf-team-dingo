from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# def index(request):
# 	return HttpResponse ("This is just a text response, unrelated to the database.")


def books(request):
    books = Book.objects.all()
    return render(request, 'core/books.html', {'books': books})


def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, "pk": pk})


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
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
        if form.is_valid():
            book = form.save()
            form.save()
            return redirect('books', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'core/new_book.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete
    return redirect('/')

