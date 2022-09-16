# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Question, Answer


def index(request):
    question_list = Question.objects.order_by('-create_date')
    content = {"question_list": question_list}
    return render(request, 'pybo/question_list.html', content)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id = question.id)