from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo, TodoDetail
from .serializers import TodoSerializer, TodoDetailSerializer


class TodoListAPIView(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        todo_serializer = TodoSerializer(instance=todo, many=True)

        return Response(data=todo_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.validated_data["user"] = request.user
            result_data = todo_serializer.create(todo_serializer.validated_data)
            result_serializer = TodoSerializer(instance=result_data)
            return Response(data=result_serializer.data, status=status.HTTP_200_OK)

        return Response(data=todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
