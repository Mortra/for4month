from django.db import models



class Anime(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    ganre = models.CharField(max_length=255)


