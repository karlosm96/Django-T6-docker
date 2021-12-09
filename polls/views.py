from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ##return render(request, 'polls/index.html')
    return HttpResponse("Welcome to my page, you are in polls page.")

def details(request, poll_id):
    return HttpResponse("You are looking at poll %s." % poll_id)


def results(request, poll_id):
    return HttpResponse("You are looking at the result of poll %s." % poll_id)