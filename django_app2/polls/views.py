from django.http import HttpResponse



def index(request):
    return HttpResponse("helloworld You're blahblah")