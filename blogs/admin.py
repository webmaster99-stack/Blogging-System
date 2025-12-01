from django.contrib import admin
from .models import Category, Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "is_featured", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["id", "title", "category__name", "status"]


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)