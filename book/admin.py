from django.contrib import admin
from.models import Book

print("in admin.py")
admin.site.register(Book)
