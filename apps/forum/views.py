from django.shortcuts import render

from apps.forum.models import Question, Answer


def index(request):
    question_list = Question.objects.filter(control=True)
    context = {
        'question_list': question_list
    }
    return render(request, "index.html", context)


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
