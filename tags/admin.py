from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
