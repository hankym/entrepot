from django.contrib import admin

from .form import ThumbnailAdminForm

# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ("name","num","sale","remain")
    list_editable = ('sale',)
    search_fields = ("name",)
    #form = ThumbnailAdminForm






from .models import Book
admin.site.register(Book,BooksAdmin)