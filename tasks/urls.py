from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),
    path('', views.tasklist, name='task-list'),
    path('yourname/<str:name>', views.yourname, name='yourname'),
    path('task/<int:id>', views.taskview, name='taskview'),
    path('newtask/', views.newtask, name='new-task'),
    path('edit/<int:id>', views.edittask, name='edit-task'),
    path('delete/<int:id>', views.deletetask, name='delete-task'),
]
