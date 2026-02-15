from django.db.models import Prefetch
from .models import Genre, Book
from django.shortcuts import redirect, render

def home(request):
# Limit to 12 books per genre
    limited_books = Book.objects.all().order_by('id')  # Do not slice here
    genres = Genre.objects.prefetch_related(Prefetch('books', queryset=limited_books))
    return render(request,'books/home.html',{'genres':genres})

def trending(request):
    return render(request,"books/trending.html")
