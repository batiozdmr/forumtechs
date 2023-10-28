from django.urls import path

from apps.forum.views import index, question_add, question_answer

urlpatterns = [
    path('', index, name="forum"),
    path('question/add/', question_add, name="question_add"),
    path('question/answer/<int:question_id>/', question_answer, name="question_answer")
]
