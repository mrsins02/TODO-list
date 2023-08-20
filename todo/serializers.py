from rest_framework import serializers

from .models import Todo, TodoDetail


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDetail
        fields = "__all__"
        extra_kwargs = {"description": {"required": "False"}, "reminder_time": {"required": "False"}, }
        read_only_fields = ['pk']


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    details = TodoDetailSerializer(required=False)
    is_done = serializers.BooleanField(default=False)

    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {"detail.description": {"write_only": "True"}}
        read_only_fields = ['pk']

    def create(self, validated_data):
        if (details := validated_data.get("details")) is not None:
            todo_detail = TodoDetail.objects.create(description=details.get("description"),
                                                    reminder_time=details.get("reminder_time"))
            todo_detail.save()
        else:
            todo_detail = None
        todo = Todo.objects.create(user=validated_data.get("user"),
                                   todo_message=validated_data.get("todo_message"),
                                   details=todo_detail,
                                   is_done=validated_data.get("is_done"), )
        todo.save()
        return todo

    def update(self, instance: Todo, validated_data):
        instance.todo_message = validated_data.get("todo_message", instance.todo_message)
        instance.is_done = validated_data.get("is_done", instance.is_done)
        if details_kwargs := validated_data.get("details"):
            details, created = TodoDetail.objects.get_or_create(**details_kwargs)
            instance.details_id = details.pk
        instance.save()
        return instance
