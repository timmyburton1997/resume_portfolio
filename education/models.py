from django.db import models

class Education(models.Model):
    title = models.TextField()
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='image/')
    beginning = models.CharField(max_length=50)
    end = models.CharField(max_length=50)