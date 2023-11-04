from django.db import models


class Menu(models.Model):
    text = models.CharField(max_length=100)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return str(self.text)
