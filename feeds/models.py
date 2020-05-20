from django.db import models
from users import models as user_models
from classes import models as class_models
from core import models as core_models


class Feed(core_models.TimeStampedModel):
    class_order = models.ForeignKey(
        class_models.ClassOrder, on_delete=models.PROTECT, blank=True, null=True
    )
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.class_order)
