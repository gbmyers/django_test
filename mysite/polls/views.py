from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, template, context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    template = 'polls/detail.html'
    context = {'question': question}
    return render(request, template, context)


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)
