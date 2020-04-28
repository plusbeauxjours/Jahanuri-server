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
        "has_previous_check_list_submitted",
        "has_later_check_list_submitted",
        "has_submited_application",
        "has_paid",
        "has_kakao_account",
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
