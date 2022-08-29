from django.contrib import admin
from book_app.models import book, authors, Shelves


admin.site.register(book)
admin.site.register(authors)
admin.site.register(Shelves)