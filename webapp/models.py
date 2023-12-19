from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def special_characters(value):
    if any(char in "!?@#$%^&*()_+={}[]|\:;'<>,./~`" for char in value):
        raise ValidationError("Введите заново без специальных символов")


def bad_words(value, prohibited_words=None):
    if prohibited_words is None:
        prohibited_words = ["fuck", "shit", "wtf"]
    for word in prohibited_words:
        if word.lower() in value.lower():
            raise ValidationError(f"Запрещенное слово: '{word}'. Уберите это слово и введите еще раз")


class Type(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class List(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name="Краткое описание",
                               validators=[special_characters, bad_words])
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание",
                                   validators=[bad_words])
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус", related_name="statuses")
    type = models.ManyToManyField(Type, verbose_name="Тип", related_name="types")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
