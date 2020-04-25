from django.contrib import admin
from . import models


@admin.register(models.CheckListCover)
class CheckListCoverAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "uuid",
        "wood_before",
        "wood_after",
        "fire_before",
        "fire_after",
        "earth_before",
        "earth_after",
        "metal_before",
        "metal_after",
        "water_before",
        "water_after",
    )


@admin.register(models.CheckListQuestion)
class CheckListQuestionAdmin(admin.ModelAdmin):
    list_display = ("elements", "question", "uuid")


@admin.register(models.CheckListAnswer)
class CheckListAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "check_list_cover",
        "element",
        "question",
        "previous_answer",
        "later_answer",
        "is_changed",
    )
