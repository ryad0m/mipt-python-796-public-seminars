from django.shortcuts import render, redirect

from app.forms import QuestionForm
from app.models import Question, Answers


def home(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = QuestionForm()
    questions = Question.objects.all()
    return render(request, 'home.html', {
        'questions': questions,
        'form': form,
    })


def question(request):
    question = Question.objects.get(id=request.GET.get('id'))

    return render(request, 'question.html', {
        'question': question,
    })
