from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100)


class Status(models.Model):
    name = models.CharField(max_length=100)


class List(models.Model):
    summary = models.TextField(max_length=100, null=True, blank=False, verbose_name="Краткое описание")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
