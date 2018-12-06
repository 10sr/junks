import unittest

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from app import models


def _create_time_of_sleep(time, id_str, note):
    return models.TimeOfSleep.objects.create(
        time_of_sleep=now, datetime=now, id_str=id_str, note=note
    )


def _create_twitter_user(id_str, username):
    return models.TwitterUser.objects.create(id_str=id_str, username=username)


class TimeOfSleepTests(TestCase):
    def test_add_record(self):
        now = timezone.now()
        tos = models.TimeOfSleep(
            time_of_sleep=now, datetime=now, id_str="12345", note="NOTE"
        )
        print(str(tos))
        return


class UserViewTests(TestCase):
    def test_user_not_exists(self):
        response = self.client.get(reverse("app:user", args=("hoe",)))
        self.assertEqual(response.status_code, 404)
        return

    def test_user_exists(self):
        _create_twitter_user("12345", "10sr")
        response = self.client.get(reverse("app:user", args=("10sr",)))
        self.assertEqual(response.status_code, 200)
        return


class TestFailure(TestCase):
    @unittest.skip("demonstrating failing and skipping")
    def test_failure(self):
        self.assertEqual(True, False)
        return
