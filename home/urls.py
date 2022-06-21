from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('report', views.report),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
    path('task/add', views.task_add),
    path('task/delete/', views.task_delete),
    path('task/update/', views.task_update),
]

