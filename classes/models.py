import uuid
from django.db import models
from users import models as user_models
from core import models as core_models


class ClassOrder(core_models.TimeStampedModel):
    order = models.IntegerField(blank=True, null=True, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.order)


class ReportCover(core_models.TimeStampedModel):
    BODY_STUDY = "body study"
    ETC = "etc"
    REPORT_TYPE = (
        (BODY_STUDY, "Body Study"),
        (ETC, "Etc"),
    )
    class_order = models.ForeignKey(
        ClassOrder, on_delete=models.PROTECT, blank=True, null=True
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_set"
    )
    report_type = models.CharField(
        choices=REPORT_TYPE, max_length=200, default=BODY_STUDY
    )

    def __str__(self):
        if self.class_order:
            return (
                str(self.class_order.order)
                + " "
                + self.user.last_name
                + " "
                + self.user.first_name
            )
        else:
            return "Etc " + self.user.last_name + " " + self.user.first_name


class Report(core_models.TimeStampedModel):

    MORNING = "morning"
    NOON = "noon"
    EVENING = "evening"
    WHEN = (
        (MORNING, "Morning"),
        (NOON, "Noon"),
        (EVENING, "Evening"),
    )
    report_date = models.DateField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    report_cover = models.ForeignKey(ReportCover, on_delete=models.CASCADE)
    saeng_sik_morning = models.CharField(max_length=200)
    saeng_sik_noon = models.CharField(max_length=200)
    saeng_sik_evening = models.CharField(max_length=200)
    amino_morning = models.CharField(max_length=200)
    amino_noon = models.CharField(max_length=200)
    amino_evening = models.CharField(max_length=200)
    sangi_so_morning = models.CharField(max_length=200)
    sangi_so_noon = models.CharField(max_length=200)
    sangi_so_evening = models.CharField(max_length=200)
    jeun_hae_jil = models.BooleanField(default=False)
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
        if self.report_cover.report_type == "etc":
            return (
                "etc "
                + self.report_cover.user.last_name
                + " "
                + self.report_cover.user.first_name
            )
        else:
            return (
                str(self.report_cover.report_type)
                + " "
                + self.report_cover.user.last_name
                + " "
                + self.report_cover.user.first_name
            )
