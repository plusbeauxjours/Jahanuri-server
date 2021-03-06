import uuid
from django.db import models
from classes import models as class_models
from core import models as core_models


class Feed(core_models.TimeStampedModel):
    class_order = models.ForeignKey(
        "classes.ClassOrder", on_delete=models.CASCADE, blank=True, null=True,  verbose_name="기수"
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="고유 번호")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="회원")
    text = models.TextField(blank=True, null=True, verbose_name="공지")

    def __str__(self):
        return str(self.class_order)

    class Meta:
        verbose_name = '공지'
        verbose_name_plural = '공지'
