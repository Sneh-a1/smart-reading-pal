from django.urls import path
from books.views import home,trending

urlpatterns = [
    path('',home,name ='home'),
    path('trending/',trending,name='trending'),
]
