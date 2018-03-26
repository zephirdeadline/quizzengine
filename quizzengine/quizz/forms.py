from django import forms
from .models import *

class QuizzForm(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = {'name'}

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'name', 'image'}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = {'type', 'text'}


#theory useless
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'