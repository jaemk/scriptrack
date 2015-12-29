from django.contrib import admin

# Register your models here.

from .models import Student, Business, Purchase

admin.site.register(Student)
admin.site.register(Business)
admin.site.register(Purchase)
