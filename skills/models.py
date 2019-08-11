from django.db import models

class Skills(models.Model):
    title = models.CharField(max_length=50)
