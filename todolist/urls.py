from django.urls import path
from todolist.models import ToDoList
from todolist.views import show_todolist

# Import fungsi register
from todolist.views import register

# Import fungsi login
from todolist.views import login_user

# Import fungsi logout
from todolist.views import logout_user

from todolist.views import create_task
from todolist.views import remove_task
from todolist.views import status_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('remove/<int:id>', remove_task, name='remove_task'),
    path('status/<int:id>', status_task, name='change_task'),
]