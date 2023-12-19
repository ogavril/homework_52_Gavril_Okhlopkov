from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class List(models.Model):
    summary = models.TextField(max_length=100, null=False, blank=False, verbose_name="Краткое описание")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус", related_name="statuses")
    type = models.ManyToManyField(Type, verbose_name="Тип", related_name="types")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
