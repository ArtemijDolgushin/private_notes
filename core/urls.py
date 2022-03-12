from django.contrib import admin
from django.urls import include, path

from core.views import index, add, delete, signup, notes_list, edit

urlpatterns = [
    path('', index, name='homepage'),
    path('add', add, name='add'),
    path('signup', signup, name='signup'),
    path('delete/<int:note_id>', delete, name='delete'),
    path('edit/<int:note_id>', edit, name='edit'),
    path('list', notes_list, name='list'),
    path('accounts/', include('django.contrib.auth.urls')),
]
