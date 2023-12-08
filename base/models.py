from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL , null=True)
    name = models.CharField(max_length=200)  #thise variables name,description represent column in database
    description = models.TextField(null=True , blank=True)#null=True means thise filled cant be blank
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-updated','-created'] #we are trying to make our newist oredr to display first

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE) # here User have (one to many relationship )like a user can have multiple messages ,but multiple messages can have only one user
    room = models.ForeignKey(Room , on_delete=models.CASCADE) # here we connect [message to room] so here message is a child modle
    body = models.TextField () #contain messages
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:50] #to show first 50 mesages

    # - Create model Topic
    # - Add field host to room
    # - Create model Message
    # - Add field topic to room
