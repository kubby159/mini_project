# Create your views here.
from django.shortcuts import render
from .models import Question, Answer


def index(request):
    question_list = Question.objects.order_by('-create_date')
    content = {"question_list": question_list}
    return render(request, 'pybo/question_list.html', content)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    content = {'question': question}
    return render(request, 'pybo/question_detail.html', content)

