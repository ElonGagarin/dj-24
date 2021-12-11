from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from books.models import Book
# from books.converters import PubDateConverter
import datetime

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    books = [{'name':i.name, 'author':i.author, 'pub_date':str(i.pub_date)} for i in books]
    context = {'books': books}
    return render(request, template, context)

def db(request):
    books = Book.objects.all()
    books = [i.name for i in books]
    return HttpResponse('<br>'.join(books))

def one_book(request, date):
    template = 'books/one_book.html'
    d = datetime.datetime.strptime(date, '%Y-%m-%d')
    # books = Book.objects.filter(pub_date = d)
    data_sort = Book.objects.order_by('pub_date')
    # books = data_sort.filter(pub_date = d)
    s = {str(s.pub_date):i+1 for i, s in enumerate(data_sort)}


    books = [{'name':i.name, 'author':i.author, 'pub_date':str(i.pub_date)} for i in data_sort]


    paginator = Paginator(books, 1)
    
    page = paginator.get_page(s[str(d.date())])

    next_ = str(d.date())
    back_ = str(d.date())

    if page.has_next():
        next_ = list(s.keys())[list(s.values()).index(int(s[str(d.date())])+1)]

    if page.has_previous():    
        back_ = list(s.keys())[list(s.values()).index(int(s[str(d.date())])-1)]


    context = {'book': page.object_list[0],
                'page': page,
                'data_next': next_,
                'data_back': back_
                }
    print(context)
    return render(request, template, context)

