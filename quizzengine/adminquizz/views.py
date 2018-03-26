from django.shortcuts import render

from adminquizz.Libs.security import *
from .forms import *


# Create your views here.
@checkSignin
def adminQuizz(request):
    print(request.session['id'])
    quizz=Quizz.objects.filter(user_id=request.session['id'])
    print(str(len(quizz)))
    return render(request, 'adminquizz/adminquizz.html', {'quizz': quizz})

@checkSignin
def addQuizz(request):
    if request.method == 'POST':
        form = QuizzForm(request.POST)
        if form.is_valid() :
            quizz = form.save(commit=False)
            quizz.user_id = request.session['id']
            try:
                quizz.save()
                print("Success to save quizz")
                return HttpResponseRedirect('/adminquizz/')
            except Exception as e:
                print("Fail to save " + str(e))
        else:
            print("Fail to Save")

    form = QuizzForm()
    return render(request, 'adminquizz/addquizz.html', {'form': form})

@checkSignin
def delQuizz(request, id):
    Quizz.objects.get(id=id).delete()
    return HttpResponseRedirect('/adminquizz/')

@checkSignin
def upQuizz(request, id):
    quizz = Quizz.objects.get(id=id)
    if request.method == 'POST':
        form = QuizzForm(request.POST, instance=quizz)
        if form.is_valid() :
            quizz = form.save(commit=False)
            quizz.user_id = request.session['id']
            try:
                quizz.save()
                print("Success to save quizz")
                return HttpResponseRedirect('/adminquizz/')
            except Exception as e:
                print("Fail to save " + str(e))
        else:
            print("Fail to Save")

    form = QuizzForm(instance=quizz)
    questions = Question.objects.filter(quizz_id=id)
    uniqueAnswerTrue = {}
    for q in questions:
        try:
            Answer.objects.get(question=q, type=True)
            uniqueAnswerTrue[q.id] = True
        except:
            uniqueAnswerTrue[q.id] = False

    return render(request, 'adminquizz/updatequizz.html', {'form': form, 'id': id, 'questions': questions, 'uniqueAnswerTrue': uniqueAnswerTrue})

@checkSignin
def addQuestion(request, id):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid() :
            question = form.save(commit=False)
            question.user_id = request.session['id']
            question.quizz_id = id
            try:
                question.save()
                print("Success to save question")
                idQuestion = Question.objects.get(name=question.name, user_id= question.user_id, quizz_id=id)
                return HttpResponseRedirect('/adminquizz/addanswer/'+str(idQuestion.id))
            except Exception as e:
                print("Fail to save " + str(e))
        else:
            print("Fail to Save")
    
    form = QuestionForm()
    return render(request, 'adminquizz/addquestion.html', {'id': id, 'form': form})

@checkSignin
def delQuestion(request, idQuizz, idQuestion):
    return render(request, 'adminquizz/adminquizz.html')

@checkSignin
def upQuestion(request, idQuestion):
    question = Question.objects.get(id=idQuestion)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            try:
                question.save()
                print("Success to save quizz")
                return HttpResponseRedirect('/adminquizz/')
            except Exception as e:
                print("Fail to save " + str(e))
        else:
            print("Fail to Save")

    form = QuestionForm(instance=question)
    responses = Answer.objects.filter(question_id=idQuestion)
    return render(request, 'adminquizz/upquestion.html', {'form': form, 'idQuestion': idQuestion, 'responses': responses})

@checkSignin
def upAnswer(request, idAnswer):
    answer = Answer.objects.get(id=idAnswer)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            try:
                answer.save()
                print("Success to update answer")
                return HttpResponseRedirect('/adminquizz/')
            except Exception as e:
                print("Fail to update " + str(e))
        else:
            print("Fail to update")

    form = AnswerForm(instance=answer)
    return render(request, 'adminquizz/upanswer.html', {'form': form, 'idAnswer': idAnswer})

@checkSignin
def addAnswer(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid() :
            answer = form.save(commit=False)
            answer.question_id = id
            try:
                answer.save()
                print("Success to save answer")
                return HttpResponseRedirect('/adminquizz/addanswer/'+str(id))
            except Exception as e:
                print("Fail to save " + str(e))
        else:
            print("Fail to Save")

    form = AnswerForm()
    return render(request, 'adminquizz/addanswer.html', {'form': form, 'id': id})