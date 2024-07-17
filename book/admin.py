from django.contrib import admin

# Register your models here.
from .models import book

# Register the pet table
admin.site.register(book)