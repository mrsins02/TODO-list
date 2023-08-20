from django.urls import path
from .views import TodoListCreateAPIView,TodoDetailAPIView
urlpatterns = [
    path('', TodoListCreateAPIView.as_view(),name="todo_list"),
    path('todo-detail/<int:pk>/', TodoDetailAPIView.as_view(),name="todo_detail"),
]