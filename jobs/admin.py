from django.contrib import admin

from .models import Job
# Register your models here.

# add here all the models to show up to the admin page

admin.site.register(Job)
