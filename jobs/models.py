from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    githublink = models.CharField(max_length=100, default="")
    hostedprojecturl = models.CharField(max_length=100, default="")
    jobtitle = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.jobtitle
