from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo, TodoDetail
from .serializers import TodoSerializer, TodoDetailSerializer


class TodoListAPIView(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        todo_ser = TodoSerializer(instance=todo, many=True)

        return Response(data=todo_ser.data, status=status.HTTP_200_OK)
