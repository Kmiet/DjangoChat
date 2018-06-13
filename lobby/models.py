from django.db import models

# Create your models here.
class ChannelManager(models.Manager):

    def create_channel(self, name):
        if len(name) > 16:
            raise ValueError('Name must be at most 16 characters long')
        channel = self.model(name=name.title())
        channel.save()
        return channel

class Channel(models.Model):
    name = models.CharField(max_length=16, unique=True)

    objects = ChannelManager()

    def __str__(self):
        return self.name