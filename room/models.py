from django.db import models
from floor.models import Floor

class Room(model.Model):

    number = models.IntegerField()
    
    floor = models.ForeignKey(Floor, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.number)
    
