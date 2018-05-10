from django.db import models


class Question(models.Model):
    text = models.TextField()


class Answers(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
