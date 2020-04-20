from django.contrib import admin
from . import models


@admin.register(models.ReportCover)
class CheckListCoverAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "report_type",
        "order",
        "start_date",
        "end_date",
    )


@admin.register(models.Report)
class CheckListQuestionAdmin(admin.ModelAdmin):
    list_display = ("report_cover", "created_at")
