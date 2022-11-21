from django.db import models
from room.models import Room

class Card(models.Model):

    cardId = models.CharField(max_length=20)

    room = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)

    macAddress = models.CharField(max_length=20)

    startTimeValid = models.DateTimeField()

    endTimeValid = models.DateTimeField()


    def __str__(self):
        return f"{self.cardId} - {self.room.number}"
    