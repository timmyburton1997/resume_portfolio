from django.db import models

class Volunteering(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField()
    summary = models.CharField(max_length=1000)
    time = models.TextField()
    extra = models.TextField()

