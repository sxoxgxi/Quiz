from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from .models import Questions
# Create your views here.


def Home(request):
    return HttpResponse("hello world!")


def Quizes(request):
    try:
        quizes = Questions.objects.all()
        data = [{'category': quiz.category, 'question': quiz.question,
                 'score': quiz.score} for quiz in quizes]
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as uwu:
        print(uwu)
    return HttpResponse("ohh no something is wrong!!")
