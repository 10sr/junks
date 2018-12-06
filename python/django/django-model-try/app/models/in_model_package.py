from django.db import models


# makemigrations はこのパッケージを発見できないらしい
# https://docs.djangoproject.com/en/2.1/topics/db/models/#using-models

class CModel(models.Model):
    afield = models.CharField(max_length=50)

    note = models.CharField(max_length=500, default="")

    def __str__(self):
        return f"{self.afield}/{self.note}"

    @property
    def str(self):
        return str(self)
