from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=255)
    title = models.TextField()
    time = models.TextField()
    send = models.FileField()