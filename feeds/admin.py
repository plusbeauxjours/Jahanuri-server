from django.contrib import admin
from . import models


@admin.register(models.Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("class_order", "text")
