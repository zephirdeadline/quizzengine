from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^adminquizz/$', views.adminQuizz),
url(r'^adminquizz/addquizz/$', views.addQuizz),

url(r'^adminquizz/updatequizz/(?P<id>[0-9]+)$', views.upQuizz),

url(r'^adminquizz/upquestion/(?P<idQuestion>[0-9]+)$', views.upQuestion),

url(r'^adminquizz/delete/(?P<id>[0-9]+)$', views.delQuizz),
url(r'^adminquizz/upanswer/(?P<idAnswer>[0-9]+)$', views.upAnswer),
url(r'^adminquizz/addanswer/(?P<id>[0-9]+)$', views.addAnswer),
url(r'^adminquizz/addquestion/(?P<id>[0-9]+)$', views.addQuestion)
]
