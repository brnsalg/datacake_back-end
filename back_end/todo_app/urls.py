from django.urls import re_path
from todo_app import views

urlpatterns = [
    re_path(r'^todo/$', views.todoApi),
    re_path(r'^todo/([0-9]+)$', views.todoApi)
]