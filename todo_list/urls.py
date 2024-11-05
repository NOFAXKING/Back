from django.urls import path
from .views import NoteView, NoteListView

todo_urlpatterns = [
    path('todos/', NoteListView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', NoteView.as_view(), name='todos'),
]
