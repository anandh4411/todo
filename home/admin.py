from django.contrib import admin
from home.models import Task, User
from django.utils.html import format_html, urlencode
from django.urls import reverse 
from django.db.models import Count


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'task_count', 'password']

    @admin.display(ordering='task_count')
    def task_count(self, user):
        url = (
        reverse('admin:home_task_changelist') 
        + '?' 
        + urlencode({
            'user__id': str(user.id)
        }))
        return format_html('<a href="{}">{}</a>', url, user.task_count)
 
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            task_count = Count('task')
        )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'estimated_time', 'elapsed_time', 'user']