from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('create-book-page',views.create_book,name='create_book_page'),
]

