from django.contrib import admin
from . import models


@admin.register(models.ClassOrder)
class ClassOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "start_date", "end_date")


@admin.register(models.ReportCover)
class ReportCoverAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "report_type",
        "class_order",
    )


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("report_cover", "types",
                    "report_date", "created_at")


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("user", "has_married",
                    "has_childbirth", "agree_personal_information", "confirm")


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "birth_date",
                    "job", "phone_number", "email_address", "confirm")
