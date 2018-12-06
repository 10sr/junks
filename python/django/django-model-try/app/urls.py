from django.conf.urls import include, url

# from django.contrib.auth import views as auth_views

from app import views

app_name = "app"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(
        r"^login_required_page$", views.login_required_page, name="login_required_page"
    ),
]
