from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'deadline', 'is_done')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
