from django.db import models

# Create your models here.
class UrlShoartner(models.Model):
    url=models.CharField(max_length=5)
    shorturl=models.CharField(max_length=100)


    def __str__(self):
        return self.url