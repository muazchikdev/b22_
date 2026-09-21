from django.contrib import admin
from .models import Genre, Author, Book
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Register your models here.


# @admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','get_image')
    search_fields = ('id','name',)
    list_per_page = 5

    @admin.display(description=_('Изображения'))
    def get_image(self,genre):
        if genre.image:
            return mark_safe(
                f'<img src="{genre.image.url}" alt="{genre.name}"width="100px", height="100px" />')




# @admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date','get_image')
    search_fields = ('full_name',)
    list_per_page = 6

    @admin.display(description=_('Фото Автора'))
    def get_image(self,authur):
        if authur.image:
            return mark_safe(
                f'<img src="{authur.image.url}" alt="{authur.full_name}"width="100px", height="100px" />')


# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre','author','part','created_at')
    list_filter = ('genre', 'author')
    search_fields = ('title',)
    list_per_page = 10






admin.site.register(Genre,GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)