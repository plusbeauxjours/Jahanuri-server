from django.contrib import admin
from . import models


@admin.register(models.Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("user", "class_order", "text", "created_at")
    search_fields = ('user__username', 'user__first_name',
                     'user__last_name', 'text',)
    list_filter = ('class_order', )
