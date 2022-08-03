from django.db import models
from helpers.models import BaseModel
from common.models import User
# Create your models here.


class Message(BaseModel):
    text = models.TextField()
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)