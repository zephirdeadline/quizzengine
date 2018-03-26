from django.shortcuts import render
from django.db import transaction
from .forms import *
from django.http import HttpResponseRedirect
from hashlib import sha1

# Create your views here.

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/login/signin')


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = sha1(str(user.password).encode()).hexdigest()
            if User.objects.filter(email=user.email, password=user.password).exists():
                print("Success to Login")
                user = User.objects.get(email=user.email, password=user.password)
                request.session['id'] = user.id
                return HttpResponseRedirect('/adminquizz/')
            else:
                print('user not exist')
        else:
            print("Fail to valid form")

    form = SigninForm()
    return render(request, 'login/signin.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user = form.save(commit=False)
        user.password = sha1(str(user.password).encode()).hexdigest()
        if form.is_valid() and not User.objects.filter(email=user.email).exists():
            try:
                user.save()
                print("Success to register")
                request.session['id'] = user.id
                return HttpResponseRedirect('/adminquizz/')
            except Exception as e:
                print("Fail to save " + str(e))
        else:
            print("Fail to Register")

    form = SignupForm()
    return render(request, 'login/signup.html', {'form': form})