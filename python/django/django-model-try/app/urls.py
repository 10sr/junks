from django.conf.urls import include, url

# from django.contrib.auth import views as auth_views

from app import views

app_name = "app"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(
        r"^login_required_page$", views.login_required_page, name="login_required_page"
    ),
    # TODO: Fix URL to use
    # TODO: Use this
    # https://docs.djangoproject.com/en/2.1/releases/2.0/#simplified-url-routing-syntax
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)$", views.user, name="user"),
    url(
        r"^user/(?P<username>[_0-9a-zA-Z]+)/addneru$",
        views.user_addneru,
        name="user_addneru",
    ),
    # pk is for primary key so URL like usesrview/10sr will fail
    # TODO: How to pass arbitrary parameter to DetailView?
    url(r"^userview/(?P<pk>[_0-9a-zA-Z]+)$", views.UserView.as_view(), name="userview"),
]
