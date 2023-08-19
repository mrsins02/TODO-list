from django.urls import path
from .views import TodoListAPIView
urlpatterns = [
    path('', TodoListAPIView.as_view(),name="todo_list"),
]