from django.contrib import admin
from . import models


@admin.register(models.CheckListCover)
class CheckListCoverAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
    )


@admin.register(models.CheckListQuestion)
class CheckListQuestionAdmin(admin.ModelAdmin):
    list_display = ("elements", "question")


@admin.register(models.CheckListAnswer)
class CheckListAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "check_list_cover",
        "question",
        "previous_answer",
        "later_answer",
        "is_changed",
    )
