from django.db import models
from enum import Enum

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
    description = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices(), default=Status.PENDING.value)
    priority = models.IntegerField(choices=Priority.choices(), default=Priority.LOW.value)
    image_path = models.ImageField(upload_to='images/', null=True, blank=True)
