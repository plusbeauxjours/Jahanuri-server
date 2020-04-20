import uuid
from django.db import models
from users import models as user_models
from core import models as core_models


class ReportCover(core_models.TimeStampedModel):
    BODY_STUDY = "body study"
    ETC = "etc"
    REPORT_TYPE = (
        (BODY_STUDY, "Body Study"),
        (ETC, "Etc"),
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    report_type = models.CharField(choices=REPORT_TYPE, max_length=200)
    order = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.order) + self.user.last_name + self.user.first_name


class Report(core_models.TimeStampedModel):

    MORNING = "morning"
    NOON = "noon"
    EVENING = "evening"
    WHEN = (
        (MORNING, "Morning"),
        (NOON, "Noon"),
        (EVENING, "Evening"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    report_cover = models.ForeignKey(ReportCover, on_delete=models.CASCADE)
    sang_sik = models.CharField(choices=WHEN, max_length=200, blank=True, null=True)
    amino = models.CharField(choices=WHEN, max_length=200, blank=True, null=True)
    sangi_so = models.CharField(choices=WHEN, max_length=200, blank=True, null=True)
    jeun_hae_jil = models.BooleanField(default=False)
    jeun_hae_jil_time = models.TimeField(blank=True, null=True)
    meal = models.CharField(max_length=1000)
    meal_check = models.CharField(max_length=1000)
    sleeping = models.CharField(max_length=1000)
    stool = models.CharField(max_length=1000)
    hot_grain = models.CharField(max_length=1000)
    hot_water = models.CharField(max_length=1000)
    strolling = models.CharField(max_length=1000)
    workout = models.CharField(max_length=1000)
    lecture = models.CharField(max_length=1000)
    etc = models.CharField(max_length=1000)
    diary = models.CharField(max_length=5000)

    def __str__(self):
        return self.question
