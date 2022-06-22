from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from .models import Questions
# Create your views here.


def Home(request):
    return HttpResponse("hello world!")
