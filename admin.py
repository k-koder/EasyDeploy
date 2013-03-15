from django.contrib import admin 
from cxlsite.books.models import Book, Author, Publisher 
admin.site.register(Book) 
admin.site.register(Publisher) 
admin.site.register(Author)