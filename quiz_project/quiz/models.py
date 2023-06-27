from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    personality_type = models.CharField(max_length=255)


class UserAnswer(models.Model):
    user_id = models.IntegerField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
