from django.db import models
from enum import Enum
from django.contrib.auth.models import User
import os
import uuid

class Status(Enum):
    PENDING = 0
    DOING = 10
    DONE = 20

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
        

class Priority(Enum):
    LOW = 0
    MEDIUM = 10
    HIGH = 20
    URGENT = 30

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Task(models.Model):
    def get_image_path(instance, filename):
        unique_id = uuid.uuid4().hex
        if instance.user:
            return os.path.join(f'images/user_{instance.user.id}', f'{unique_id}.jpg')  
        return os.path.join('images/', f'{unique_id}.jpg') 
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_task', null=True)
    description = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices(), default=Status.PENDING.value)
    priority = models.IntegerField(choices=Priority.choices(), default=Priority.LOW.value)
    image_path = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.get_status_display()}"