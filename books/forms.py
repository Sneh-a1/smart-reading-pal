from django import forms 
from books.models import Book

class RatingWidget(forms.NumberInput):
    
    def __init__(self, attrs=None):
        default_attrs = {
            'type': 'number',
            'step': '0.5',
            'min': '0',
            'max': '5',
            'placeholder': 'Give your ratings (0-5)'
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','description','genre','IBSN','publication_date','average_rating']
        labels={
            'title':'Title',
            'author':'Author',
            'description':'Description',
            'genre':'Genre',
            'IBSN':'ISBN',
            'publication_date':'Publication Date',
            'average_rating':'Average Rating',
        }
        widgets={
            'publication_date':forms.DateInput(attrs={'type': 'date'}),
            'average_rating':RatingWidget(),
    
        }
       
        