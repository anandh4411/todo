from django.contrib import admin
from home.models import Task, User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'password']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id']