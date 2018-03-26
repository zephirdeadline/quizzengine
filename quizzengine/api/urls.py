from . import views
from django.conf.urls import url

urlpatterns = [
url(r'^api/score/(?P<hash>\w+)$', views.getScore),

]
