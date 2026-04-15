from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Home Page of Blog App')


def about(request):
    return HttpResponse('<h1> About Page of Blog App')