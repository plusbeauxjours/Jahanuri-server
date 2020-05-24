import uuid
from django.db import models
from users import models as user_models
from core import models as core_models


class ClassOrder(core_models.TimeStampedModel):
    order = models.IntegerField(blank=True, null=True, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

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
        ClassOrder,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="class_order_set",
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
    saeng_sik_morning = models.CharField(max_length=200, blank=True, null=True)
    saeng_sik_noon = models.CharField(max_length=200, blank=True, null=True)
    saeng_sik_evening = models.CharField(max_length=200, blank=True, null=True)
    amino_morning = models.CharField(max_length=200, blank=True, null=True)
    amino_noon = models.CharField(max_length=200, blank=True, null=True)
    amino_evening = models.CharField(max_length=200, blank=True, null=True)
    sangi_so_morning = models.CharField(max_length=200, blank=True, null=True)
    sangi_so_noon = models.CharField(max_length=200, blank=True, null=True)
    sangi_so_evening = models.CharField(max_length=200, blank=True, null=True)
    jeun_hae_jil_a = models.BooleanField(default=False)
    jeun_hae_jil_b = models.BooleanField(default=False)
    jeun_hae_jil_c = models.BooleanField(default=False)
    jeun_hae_jil_d = models.BooleanField(default=False)
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

    def jeun_hae_jil(self):
        jeun_hae_jil = (
            self.jeun_hae_jil_a
            + self.jeun_hae_jil_b
            + self.jeun_hae_jil_c
            + self.jeun_hae_jil_d
        )
        return jeun_hae_jil.count()

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


class Survey(core_models.TimeStampedModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    has_married = models.BooleanField(default=False)
    has_married_etc = models.CharField(max_length=2000, null=True, blank=True)
    has_childbirth = models.BooleanField(default=False)
    has_childbirth_etc = models.CharField(max_length=2000, null=True, blank=True)
    how_many_child = models.CharField(max_length=2000, null=True, blank=True)
    status = models.CharField(max_length=2000, null=True, blank=True)
    change = models.CharField(max_length=2000, null=True, blank=True)
    agree_personal_information = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)


class Application(core_models.TimeStampedModel):
    GENDER_MALE = "GENDER_MALE"
    GENDER_FEMALE = "GENDER_FEMALE"
    GENDER_OTHER = "GENDER_OTHER"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=20, null=True, blank=True
    )
    job = models.CharField(max_length=200)
