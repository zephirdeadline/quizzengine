from . import views
from django.conf.urls import url

urlpatterns = [
url(r'^$', views.signin),
    url(r'^login/signup/$', views.signup),
    url(r'^login/signin/$', views.signin),
    url(r'^login/logout/$', views.logout)
]
