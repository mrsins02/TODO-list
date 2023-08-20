from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from .models import Todo, TodoDetail
from .serializers import TodoSerializer, TodoDetailSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.query_params.get("is_done") == "true":
            queryset = Todo.objects.filter(user=self.request.user, is_done=True)
        elif self.request.query_params.get("is_done") == "false":
            queryset = Todo.objects.filter(user=self.request.user, is_done=False)
        else:
            queryset = Todo.objects.filter(user=self.request.user).order_by("is_done")
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["user"] = request.user
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        todo = get_object_or_404(Todo, id=self.kwargs.get("pk"),
                                 user=self.request.user)
        return todo

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance).data
        self.perform_destroy(instance)
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)
