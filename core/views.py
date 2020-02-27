from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# def index(request):
# 	return HttpResponse ("This is just a text response, unrelated to the database.") 

def books(request):
	books = Book.objects.all()
	return render(request, 'core/books.html', {'books':books})

def new_book(request):
		if request.method == "POST":
			form = BookForm(request.POST)
			if form.is_valid():
				book = form.save()
				return redirect('books')
		else:
			form = BookForm()

		return render(request, 'core/new_book.html', {'form': form})

