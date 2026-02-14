from django.contrib import admin
from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'average_rating')
    search_fields = ('title', 'author')
    list_filter = ('genre',)
