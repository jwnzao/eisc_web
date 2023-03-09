from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    body = models.TextField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver"
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[:50]


# class Conversation(models.Model):
#     messages = models.ManyToOneRel()
