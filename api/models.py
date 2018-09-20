from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def _str_(self):
        return f'{self.title} - {self.artist}'
