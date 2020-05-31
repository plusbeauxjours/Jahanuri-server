from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "class_order",
        "first_name",
        "last_name",
        "gender",
        "has_submitted_previous_check_list",
        "has_submitted_later_check_list",
        "has_submitted_habit_check_list",
        "has_submitted_application",
        "has_submitted_survey",
        "has_paid",
        "has_apple_account",
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
