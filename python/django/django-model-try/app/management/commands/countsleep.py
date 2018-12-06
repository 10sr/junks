from django.core.management.base import BaseCommand, CommandError

from app.models import TimeOfSleep


class Command(BaseCommand):
    help = "Count sleep record num"

    def add_arguments(self, parser):
        return

    def handle(self, *args, **kargs):
        self.stdout.write(args)
        self.stdout.write(kargs)
        self.stdout.write(TimeOfSleep.objects.count())
        return
