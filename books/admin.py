from django.contrib import admin

from .models import Book


# @admin.register(Book)
# class PostAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Book)

