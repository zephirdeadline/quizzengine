from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
import datetime


# Create your views here.
def quizz(request, idQuizz, size, hash):
    if not Quizz.objects.filter(id=idQuizz).exists():
        return HttpResponseRedirect('/')
    score = Score(hash=hash, quizz_id=idQuizz)
    if Score.objects.filter(hash=hash).exists():
        return HttpResponseRedirect("/quizz/"+idQuizz+'/'+size+'/'+str(datetime.datetime.now().microsecond))
    if int(size) < 1:
        return HttpResponseRedirect("/quizz/" + idQuizz + '/' + str(1) + '/' + str(datetime.datetime.now().microsecond))
    score.save()
    quizz = Quizz.objects.get(id = idQuizz)
    queryList = Question.objects.filter(quizz = quizz).order_by('?')
    maxQuestions = int(len(queryList))
    sizeInt = int(size)
    if sizeInt > maxQuestions:
        maxQuestions = sizeInt
    else:
        maxQuestions = sizeInt
        print('mooore')
    questions = queryList[:maxQuestions]
    responses = {}

    for q in questions:
        ScoreToQuestion(score=score, question=q).save()
        responses[q.id] = Answer.objects.filter(question = q)
    return render(request, 'quizz/quizz.html', {'quizz': quizz, 'questions': questions, 'responses': responses, 'hash': hash})


def quizzresult(request, hash):
    score = Score.objects.get(hash=hash)
    questions = ScoreToQuestion.objects.filter(score=score)
    if request.method == 'POST':
        good = 0
        total = 0
        correction = {}
        for q in questions:
            total += 1
            if request.POST.get(str(q.question_id), '') == 'True':
                good += 1
            else:
                if request.POST.get(str(q.question_id), '') != '':
                    questionFail = Question.objects.get(id=q.question_id)
                    correction[questionFail.name] = Answer.objects.get(question_id=questionFail.id, type=True)

        final = good * 20 / total
        score.totalQuestions = total
        score.point = good
        score.save()
        return render(request, 'quizz/quizzresult.html', {'correction': correction, 'good': good, 'total': total, 'final': final})
    return HttpResponseRedirect('/quizz/'+str(questions.first().question.quizz.id)+'/'+str(score.totalQuestions)+'/'+str(datetime.datetime.now().microsecond))

