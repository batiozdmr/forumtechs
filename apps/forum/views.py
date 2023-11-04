from django.shortcuts import render

from apps.forum.models import Question, Answer
from django.contrib.auth.decorators import login_required

from apps.parameter.models import Menu


def index(request):
    question_list = Question.objects.filter(control=True)
    menu_list = Menu.objects.filter()
    context = {
        'question_list': question_list,
        'menu_list': menu_list
    }
    return render(request, "index.html", context)


@login_required
def question_add(request):
    if request.POST:
        text = request.POST.get("text")
        control = Question.objects.create(text=text, user=request.user)
        if control:
            print("Kayıt Başarılı")
        else:
            print("Teknik bir hata oluştu")
    context = {

    }
    return render(request, "question_add.html", context)


@login_required
def question_answer(request, question_id):
    if request.POST:
        text = request.POST.get("text")
        control = Answer.objects.create(text=text, user=request.user, question_id=question_id)
        if control:
            print("Kayıt Başarılı")
        else:
            print("Teknik bir hata oluştu")
    context = {

    }
    return render(request, "question_answer.html", context)
