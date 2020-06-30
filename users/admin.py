from django.contrib import admin
from . import models
from classes import models as class_models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    actions = ['update_has_paid']
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
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('class_order', 'has_paid', 'gender',
                   'has_apple_account', 'has_submitted_application')

    def update_has_paid(self, request, queryset):
        class_order = class_models.ClassOrder.objects.last()
        queryset.update(has_paid=True, class_order=class_order)

    update_has_paid.short_description = "💳결제"
