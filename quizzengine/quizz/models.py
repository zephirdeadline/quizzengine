from django.db import models

# Create your models here.

class Quizz(models.Model):
    user = models.ForeignKey('login.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    level = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)

class Question(models.Model):
    user = models.ForeignKey('login.User')
    quizz = models.ForeignKey('Quizz')
    name = models.TextField()
    image = models.FileField(upload_to='static/upload/', blank=True, null=True)

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    type = models.BooleanField()
    text = models.CharField(max_length=256)

class Score(models.Model):
    point = models.IntegerField(default=-1)
    quizz = models.ForeignKey('Quizz')
    date = models.DateField(auto_now_add=True)
    #quizz = models.ForeignKey('Quizz')
    hash = models.CharField(max_length=64, unique=True)
    totalQuestions = models.IntegerField(default=-1)

# Mandatory because Random Question
class ScoreToQuestion(models.Model):
    score = models.ForeignKey('Score')
    question = models.ForeignKey('Question')