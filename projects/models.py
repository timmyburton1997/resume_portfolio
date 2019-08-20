from django.db import models

class Projects(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField()
    time = models.FileField(upload_to='images/')
    extra = models.TextField()
