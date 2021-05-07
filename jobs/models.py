from django.db import models

# Create your models here.


# inside of the media folder when anyone uploads then the thing should move in to the upload_to folder we specified

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)