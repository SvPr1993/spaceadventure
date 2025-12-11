from django.db import models


class Font(models.Model):
    font_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.font_name}'


class KeplerUser(models.Model):
    user_name = models.CharField(max_length=21)
    font = models.ForeignKey(Font, on_delete=models.PROTECT)
