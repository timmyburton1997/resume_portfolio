from django.db import models

class Education(models.Model):
    title = models.TextField()
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='image/')
