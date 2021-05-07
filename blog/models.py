from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')

    # this is for changing the name in the admin page
    def __str__(self):
        return self.title


    # here this function is for a return of first 100 words of the body-> just in case we want to avoid it being too long
    def summary(self):
        return self.body[:100]
    
    # this is for the change of the format of time to what we want
    def pub_date_change(self):
        return self.pub_date.strftime('%b %e %Y')
