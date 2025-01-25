from django.db import models
from django.shortcuts import reverse

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_detail_url(self):
        return reverse('lessons:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('lessons:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('lessons:update', args=[self.pk])

    def __str__(self):
        return f'{self.name}'

