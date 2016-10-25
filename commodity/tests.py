from django.test import TestCase

# Create your tests here.

from django.contrib import admin

from .models import Books

admin.site.register(Books)