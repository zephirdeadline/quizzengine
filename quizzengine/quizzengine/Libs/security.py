from django.http import HttpResponseRedirect

def isConnected(request):
    return 'id' in request.session


def checkSignin(func):
    def check(*args, **kwargs):
        if not isConnected(args[0]):
            return HttpResponseRedirect('/')
        return func(*args, **kwargs)
    return check

