from django.db import models


class TimeOfSleep(models.Model):
    time_of_sleep = models.DateTimeField("Time Of Sleep")
    datetime = models.DateTimeField("Time when record inserted")
    # Twitter id in number
    id_str = models.CharField(max_length=50)

    note = models.CharField(max_length=500, default="")

    def __str__(self):
        return "id_str: {}, tos: {}, record time: {}, note: {}".format(
            self.id_str, self.time_of_sleep, self.datetime, self.note
        )

    def get_screenname(self):
        n = TwitterUsername.get(id_str=self.id_str)
        return n.username

    @property
    def str(self):
        return str(self)


class TwitterUser(models.Model):
    # Twitter id in number
    id_str = models.CharField(max_length=50)
    id_str2 = models.CharField(max_length=50)
    # Twitter screen name
    # TODO: screen_name is better?
    username = models.CharField(max_length=20)

    def __str__(self):
        return "id_str: {}, username: {}".format(self.id_str, self.username)

    @property
    def str(self):
        return str(self)
