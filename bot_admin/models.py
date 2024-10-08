from django.db import models

class Channel(models.Model):
    channel_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    video_file_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.username} ({self.telegram_id})'