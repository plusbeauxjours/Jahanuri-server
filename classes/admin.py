from django.contrib import admin
from . import models


@admin.register(models.ClassOrder)
class ClassOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "start_date", "end_date", "uuid")


@admin.register(models.ReportCover)
class ReportCoverAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "report_type",
        "class_order",
        "uuid",
    )


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("report_cover", "created_at", "report_date", "uuid")


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("user", "agree_personal_information", "confirm")


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "birth_date", "job", "phone_number", "confirm")
