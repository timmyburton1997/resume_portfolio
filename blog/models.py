from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField()
    body = models.CharField(max_length=1000)
    time = models.DateTimeField()
    summary = models.CharField(max_length=255)
    blog_num = models.CharField(max_length=255)


    def __str__(self):
        return self.blog_num