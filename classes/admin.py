from django.contrib import admin
from . import models


@admin.register(models.ClassOrder)
class ClassOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "start_date", "end_date")
    search_fields = ('order',)


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
    search_fields = ('user__username', 'user__first_name',
                     'user__last_name',)


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("user", "has_married",
                    "has_childbirth", "agree_personal_information", "confirm")
    search_fields = ('user__username', 'user__first_name',
                     'user__last_name', 'has_married_etc',
                     'has_childbirth_etc',
                     'status',
                     'change')
    list_filter = ('has_married', 'has_childbirth',)


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "birth_date",
                    "job", "phone_number", "email_address", "confirm")
    search_fields = ('user__username', 'user__first_name',
                     'user__last_name', 'email_address', 'address', 'approach_etc', 'phone_number', 'job')
    list_filter = ('gender', 'approach',)
