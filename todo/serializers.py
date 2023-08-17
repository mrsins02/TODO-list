from rest_framework import serializers
from .models import Todo, TodoDetail


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDetail
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    details = TodoDetailSerializer()

    class Meta:
        model = Todo
        fields = "__all__"
