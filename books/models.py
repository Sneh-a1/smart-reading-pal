from django.db import models
from decimal import Decimal
from django.core.validators import RegexValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    GENRE_CHOICES=[
        ('classics','Classics'),
        ('books-we-love','Books We Love'),
        ('sci-fi','Sci-Fi'),
        ('science','Science'),
        ('history','History'),
        ('romance','Romance'),
        ('thriller','Thriller'),
        ('kids','Kids books'),
    ]
    
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.TextField()
    genre_text= models.CharField(max_length=75,choices=GENRE_CHOICES)
    IBSN=models.DecimalField(max_digits=13,decimal_places=0)
    publication_date=models.DateField()
    average_rating=models.DecimalField(max_digits=3, decimal_places=1, default=Decimal('0.0'))
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True,related_name='books')



