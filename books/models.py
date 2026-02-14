from django.db import models
from decimal import Decimal

# Create your models here.
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
    genre= models.CharField(max_length=75,choices=GENRE_CHOICES)
    IBSN=models.DecimalField(max_digits=13,decimal_places=0)
    publication_date=models.DateField()
    average_rating=models.DecimalField(max_digits=3, decimal_places=1, default=Decimal('0.0'))
