from django.contrib import admin
from .models import *


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """ Опросы """
    list_display = [field.name for field in Survey._meta.fields]  # все поля выводит в цикле
    search_fields = ["title", "data_start"]
    list_filter = ["title", "data_start"]


@admin.register(TypeQuestion)
class TypeQuestionAdmin(admin.ModelAdmin):
    """ Типы вопросов """
    list_display = ("id", "name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """ Типы вопросов """
    list_display = [field.name for field in Question._meta.fields]  # все поля выводит в цикле
    search_fields = ["text_question"]
    list_filter = ["text_question", "survey", "type_question"]


@admin.register(Interviewee)
class IntervieweeAdmin(admin.ModelAdmin):
    """ Пользовавтель """
    list_display = ("id",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """ Ответы """
    list_display = [field.name for field in Question._meta.fields]  # все поля выводит в цикле
    search_fields = ["user_id", "survey", "text"]
    list_filter = ["user_id", "survey", "text"]
