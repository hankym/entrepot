from django.contrib import admin

from .form import ThumbnailAdminForm

# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ("name","num")

    form = ThumbnailAdminForm






from .models import Book
admin.site.register(Book,BooksAdmin)