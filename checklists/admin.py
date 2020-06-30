from django.contrib import admin
from . import models


@admin.register(models.CheckListQuestion)
class CheckListQuestionAdmin(admin.ModelAdmin):
    list_display = ("element", "question")
    search_fields = ('element', 'question', 'uuid')
    list_filter = ('element', )


@admin.register(models.CheckListAnswer)
class CheckListAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "element",
        "question",
        "previous_answer",
        "later_answer",
        "is_changed",
    )
    search_fields = ('user__username', 'user__first_name',
                     'user__last_name', 'element', 'question__question', 'uuid')
    list_filter = ('question__element', )


@admin.register(models.HabitCheckList)
class HabitCheckListAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at"
    )
    search_fields = ('user__username', 'user__first_name',
                     'user__last_name', )
