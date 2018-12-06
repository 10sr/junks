from django.core.management.base import BaseCommand, CommandError

from app import models

_twitteruser_username = "10sr"
_twitteruser_id_str = "73722749"


class Command(BaseCommand):
    help = "Count sleep record num"

    def add_arguments(self, parser):
        return

    def handle(self, *args, **kargs):
        try:
            user = models.TwitterUser.objects.get(username=_twitteruser_username)
            self.stdout.write("TwitterUser `{}' already exists".format(user))
        except models.TwitterUser.DoesNotExist as e:
            self.stdout.write(
                "TwitterUser {} not exists, creating".format(_twitteruser_username)
            )
            models.TwitterUser(
                username=_twitteruser_username, id_str=_twitteruser_id_str
            ).save()
        # return
