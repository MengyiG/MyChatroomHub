from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    # TODO: first sort by the number of rooms in each topic
    # then sort by the name of the topic

    # sort the topics by the number of rooms in each topic
    # def total_rooms(self):
    #     return self.rooms.count()

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # order the rooms by the time they were created
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Portal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.CharField(
        max_length=100, default='https://github.com/MengyiG')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Message(models.Model):
    # build a one to many relationship between the User and Message models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # build a one to many relationship between the Room and Message models
    # if one room is deleted, all messages in that room will be deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # order the messages by the time they were created
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
