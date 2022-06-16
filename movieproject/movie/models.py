from django.db import models

# Create your models here.
class Moviemodel(models.Model):

    Releasedate=models.DateField()
    Name=models.CharField(max_length=30)
    Actor=models.CharField(max_length=20)
    Actress=models.CharField(max_length=20)
    Ratings=models.FloatField()
