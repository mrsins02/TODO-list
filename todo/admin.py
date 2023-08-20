from django.contrib import admin

from .models import Todo, TodoDetail


class TodoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user", "is_done",)
    list_editable = ("user", "is_done",)


admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoDetail)
