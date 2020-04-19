from django.contrib import admin
from . import models


@admin.register(models.User)
class CheckListCoverAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gender", "verified")
