from django.urls import path
from . import views


# base url : http://127.0.0.1:8000/

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('', views.todo_delete, name='todo_delete'),
    path('', views.todo_detail, name='todo_detail'),

]
