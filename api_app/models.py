from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    """ Опрос """
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    data_start = models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата начала')
    data_stop = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return self.title

    class Meta:
        """Вид в админке"""
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"
        ordering = ['-data_start']


class TypeQuestion(models.Model):
    """ Тип вопроса """
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Тип вопроса')

    def __str__(self):
        return self.name

    class Meta:
        """Вид в админке"""
        verbose_name = "Тип вопроса"
        verbose_name_plural = "Типы вопросов"
        ordering = ['name']


class Question(models.Model):
    """ Вопрос """
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT, verbose_name='Опрос')
    type_question = models.ForeignKey(TypeQuestion, on_delete=models.PROTECT, verbose_name='Тип вопроса')
    text_question = models.TextField(verbose_name='Текст вопроса')
    text_answer = models.TextField(verbose_name='Текст ответа')

    def __str__(self):
        return self.text_question

    class Meta:
        """Вид в админке"""
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
