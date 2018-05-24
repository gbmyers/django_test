# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('You are at the polls index.')


def detail(request, question_id):
    response = f"You're looking at question {question_id}."
    return HttpResponse(response)


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)
