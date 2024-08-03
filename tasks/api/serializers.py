from rest_framework import serializers
from ..models import Task, Status, Priority

class TaskSerializer(serializers.ModelSerializer):
        status = serializers.ChoiceField(choices=Status.choices(), default=Status.PENDING.value)
        priority = serializers.ChoiceField(choices=Priority.choices(), default=Priority.LOW.value)
        class Meta:
                model = Task
                fields = '__all__'