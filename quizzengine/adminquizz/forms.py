# -*- coding: utf-8 -*-
from django import forms
from quizz.models import *

class QuizzForm(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = ['name', 'level']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'image']
        widgets = {
            'name': forms.Textarea(attrs={'rows':2, 'cols':50})
        }
        labels = {'name': 'Question'}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['type', 'text']
        labels = {'type': 'Correct', 'text': 'Réponse'}
