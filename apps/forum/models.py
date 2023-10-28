from django.contrib.auth.models import User
from django.db import models


class QuestionTopic(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.text)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    topic = models.ForeignKey(QuestionTopic, on_delete=models.PROTECT, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(blank=True)
    control = models.BooleanField(default=False, blank=False)

    def answer_list(self):
        answer = Answer.objects.filter(question_id=self.id, control=True)
        return answer

    def __str__(self):
        return str(self.user.username) + " ---> " + str(self.text)


class Answer(models.Model):
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    control = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user.username) + " ---> " + str(self.question.text) + " ---> " + str(self.text)
