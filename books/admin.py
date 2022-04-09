from django.contrib import admin

from .models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created', 'recommended', 'is_active', )


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )


admin.site.register(Comment, CommentAdmin)
admin.site.register(Book, BookAdmin)



