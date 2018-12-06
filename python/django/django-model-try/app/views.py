import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.views import generic

# この行があると makemigrations は model を見つけられる
# model は view から参照されている必要がある？
from app.models import basics
from app.another_model_package import AModel
# 参照を外すとなくなったことになる
# from app.models.in_model_package import CModel


def index(request):
    return HttpResponse(
        f"""<p>hell, world!</p>
    <p>
    {request.user.is_authenticated}
    <a href="{reverse("login")}?next={request.path}">Login</a>
    <a href="{reverse("logout")}?next={request.path}">Logout</a>
    </p>
    <a href="{reverse("app:login_required_page")}">login_required_page</a>
    <a href="admin">admin</a>
    <a href="user/10sr">10sr</a>
    <a href="userview/10sr">10sr view</a>
        models: {AModel} {CModel} {basics.BModel}
    """
    )


@login_required
def login_required_page(request):
    return HttpResponse(
        f"""
    Hell, {request.user}!
    <a href="{reverse("app:index")}">Back to Top</a>
    """
    )
