from django.contrib import admin
from books.models import Book,Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'genre', 'average_rating')
    search_fields = ('title', 'author')
    list_filter = ('genre',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('name',)

