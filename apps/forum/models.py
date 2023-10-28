from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()
    image = models.ImageField()
    control = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username) + " ---> " + str(self.text)


class Answer(models.Model):
    text = models.TextField()
    image = models.ImageField()
    control = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user.username) + " ---> " + str(self.question.text) + " ---> " + str(self.text)
