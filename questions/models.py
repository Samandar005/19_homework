from django.db import models
from lessons.models import Lesson
from django.shortcuts import reverse

class Test(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('questions:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('questions:update', args=[self.pk])

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)