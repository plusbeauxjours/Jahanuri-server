from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="만들어진 날")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트된 날")

    class Meta:
        abstract = True
