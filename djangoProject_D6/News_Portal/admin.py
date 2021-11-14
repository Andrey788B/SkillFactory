from django.contrib import admin
from .models import Category, News, Contact

admin.site.register(Category)
admin.site.register(News)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "date")