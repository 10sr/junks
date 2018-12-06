import inspect

from django.contrib import admin
from django.db.models import Model

import app.models


# Configure site header
admin.AdminSite.site_header = "Neru Admin"

# # Register all models to admin page
# # https://docs.djangoproject.com/en/1.10/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin
# for key in dir(app.models):
#     e = getattr(app.models, key)
#     if inspect.isclass(e) and issubclass(e, Model):
#         admin.site.register(e)


class _TimeOfSleepAdmin(admin.ModelAdmin):
    # fields = ["id_str", "time_of_sleep", "note", "datetime"]
    fieldsets = [
        (None, {"fields": ["id_str", "datetime"]}),
        ("Neru info", {"fields": ["time_of_sleep", "note"]}),
    ]


admin.site.register(app.models.TimeOfSleep, _TimeOfSleepAdmin)
admin.site.register(app.models.TwitterUser)
