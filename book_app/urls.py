from django.urls import path
from book_app import views

urlpatterns = [
    path('books/',views.book,name='book_name'),
    path('authors/',views.authors,name='authors_name'),
    path('Shelves/',views.Shelves,name='Shelves_name'),
]