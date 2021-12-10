from django.shortcuts import render, HttpResponse
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'

    context = {}
    return render(request, template, context)

def db(request):
    books = Book.objects.all()
    return HttpResponse('<br>'.join(books))
