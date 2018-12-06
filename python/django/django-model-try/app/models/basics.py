from django.db import models


class BModel(models.Model):
    afield = models.CharField(max_length=50)

    note = models.CharField(max_length=500, default="")

    def __str__(self):
        return f"{self.afield}/{self.note}"

    @property
    def str(self):
        return str(self)


class FModel(models.Model):
    afield = models.CharField(max_length=50)
    bmodel = models.ForeignKey(BModel, on_delete=models.CASCADE)
