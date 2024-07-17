from django.db import models

# Create your models here.


class Dishes(models.Model):
    dishid=models.IntegerField(primary_key=True)
    dishname=models.CharField(max_length=100)
    imageurl=models.URLField(max_length=200)
    ispublished=models.BooleanField(default=False)


    def __str__(self):
        return self.dishname