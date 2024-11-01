from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    query = request.GET.get('search', '')
    books = Book.objects.filter(title__icontains=query)  # Search filter

    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'myapp/book_list.html', {'page_obj': page_obj, 'query': query})

