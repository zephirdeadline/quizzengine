from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^quizz/(?P<idQuizz>[0-9]+)/(?P<size>[0-9]+)/(?P<hash>\w+)$', views.quizz),
url(r'^quizzresult/(?P<hash>\w+)$', views.quizzresult)
]
