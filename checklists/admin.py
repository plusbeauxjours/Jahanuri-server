from django.contrib import admin
from . import models


@admin.register(models.CheckListQuestion)
class CheckListQuestionAdmin(admin.ModelAdmin):
    list_display = ("elements", "question", "uuid")


@admin.register(models.CheckListAnswer)
class CheckListAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "element",
        "question",
        "previous_answer",
        "later_answer",
        "is_changed",
    )
