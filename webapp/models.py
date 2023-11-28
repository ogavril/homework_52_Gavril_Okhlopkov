from django.db import models


# Create your models here.


class List(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
    status = models.CharField(max_length=25, choices=status_choices, default='new', verbose_name="Статус")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата выполнения")