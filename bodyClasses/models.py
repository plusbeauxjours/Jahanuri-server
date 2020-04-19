import uuid
from django.db import models
from users import models as user_models
from core import models as core_models


class ReportCover(core_models.TimeStampedModel):
    BODY_STUDY = "body study"
    ETC = "etc"
    REPORT_TYPE = (
        (BODY_STUDY, "Body study"),
        (ETC, "Etc"),
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    report_type = models.CharField(choices=REPORT_TYPE, max_length=200)

    def __str__(self):
        return self.name


class BodyClass(core_models.TimeStampedModel):

    order = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class ReportQuestion(core_models.TimeStampedModel):

    MORNING = "morning"
    NOON = "noon"
    EVENING = "evening"
    WHEN = (
        (MORNING, "Morning"),
        (NOON, "Noon"),
        (EVENING, "Evening"),
    )

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    question = models.CharField(max_length=5000)
    when = models.CharField(choices=WHEN, max_length=200)

    def __str__(self):
        return self.question


class ReportAnswer(core_models.TimeStampedModel):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    question = models.ForeignKey(ReportQuestion, on_delete=models.CASCADE)
    previous_answer = models.BooleanField(default=False)
    later_answer = models.BooleanField(default=False)

    def is_changed(self):
        return self.previous_answer != self.later_answer

    is_changed.boolean = True
