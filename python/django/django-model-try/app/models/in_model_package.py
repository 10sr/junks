from django.db import models


class CModel(models.Model):
    afield = models.CharField(max_length=50)

    note = models.CharField(max_length=500, default="")

    def __str__(self):
        return f"{self.afield}/{self.note}"

    @property
    def str(self):
        return str(self)
