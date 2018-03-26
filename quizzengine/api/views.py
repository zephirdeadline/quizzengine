from django.shortcuts import render
from quizz.models import Score
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def getScore(request, hash):
    score = Score.objects.get(hash=hash)
    data = serializers.serialize("json", [score,])
    return HttpResponse(data, content_type="application/json")
