import uuid
from django.db import models
from users import models as user_models
from feeds import models as feed_models
from core import models as core_models
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver


class ClassOrder(core_models.TimeStampedModel):
    order = models.IntegerField(
        blank=True, null=True, unique=True, verbose_name="기수")
    start_date = models.DateField(blank=True, null=True, verbose_name="시작일")
    end_date = models.DateField(blank=True, null=True, verbose_name="끝일")
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="고유 번호")

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = '1) 몸공부 기수'
        verbose_name_plural = '1) 몸공부 기수'


@receiver(post_save, sender=ClassOrder)
def create_welcome_message(sender, instance, created, **kwargs):
    if created:
        class_order = instance
        user = user_models.User.objects.get(is_superuser=True)
        feed_models.Feed.objects.create(
            user=user, class_order=class_order, text="환영합니다.")


class Report(core_models.TimeStampedModel):

    MORNING = "morning"
    NOON = "noon"
    EVENING = "evening"
    WHEN = (
        (MORNING, "Morning"),
        (NOON, "Noon"),
        (EVENING, "Evening"),
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, verbose_name="회원", related_name="report")
    report_date = models.DateField(verbose_name="일지 날짜")
    class_order = models.ForeignKey(
        ClassOrder, on_delete=models.PROTECT, related_name="report_class_order", verbose_name="기수")
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="고유 번호")
    saeng_sik_morning = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="섭생식 아침")
    saeng_sik_noon = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="섭생식 점심")
    saeng_sik_evening = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="섭생식 저녁")
    amino_morning = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="아미노 아침")
    amino_noon = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="아미노 점심")
    amino_evening = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="아미노 저녁")
    sangi_so_morning = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="생기소 아침")
    sangi_so_noon = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="생기소 점심")
    sangi_so_evening = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="생기소 저녁")
    jeun_hae_jil_a = models.BooleanField(default=False, verbose_name="전해질 1")
    jeun_hae_jil_b = models.BooleanField(default=False, verbose_name="전해질 2")
    jeun_hae_jil_c = models.BooleanField(default=False, verbose_name="전해질 3")
    jeun_hae_jil_d = models.BooleanField(default=False, verbose_name="전해질 4")
    meal = models.CharField(max_length=1000, verbose_name="일반 식사")
    meal_check = models.CharField(max_length=1000, verbose_name="식사 습관 체크")
    sleeping = models.CharField(max_length=1000, verbose_name="잠")
    stool = models.CharField(max_length=1000, verbose_name="변")
    hot_grain = models.CharField(max_length=1000, verbose_name="곡식 찜질")
    hot_water = models.CharField(max_length=1000, verbose_name="따뜻한 물")
    strolling = models.CharField(max_length=1000, verbose_name="걷기")
    workout = models.CharField(max_length=1000, verbose_name="운동")
    lecture = models.CharField(max_length=1000, verbose_name="강의")
    etc = models.CharField(max_length=1000, verbose_name="기타")
    diary = models.CharField(max_length=5000, verbose_name="세줄 일기")

    def jeun_hae_jil(self):
        jeun_hae_jil = (
            self.jeun_hae_jil_a
            + self.jeun_hae_jil_b
            + self.jeun_hae_jil_c
            + self.jeun_hae_jil_d
        )
        return jeun_hae_jil.count()

    def __str__(self):
        return str(self.class_order.order) + " " + self.user.last_name + " " + self.user.first_name

    class Meta:
        verbose_name = '2) 일지'
        verbose_name_plural = '2) 일지'


class Survey(core_models.TimeStampedModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, verbose_name="회원", related_name="survey",)
    has_married = models.BooleanField(default=False, verbose_name="결혼")
    has_married_etc = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="결혼 기타")
    has_childbirth = models.BooleanField(default=False, verbose_name="출산")
    has_childbirth_etc = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="출산 기타")
    status = models.CharField(
        max_length=5000, null=True, blank=True, verbose_name="상태")
    change = models.CharField(
        max_length=5000, null=True, blank=True, verbose_name="변화")
    agree_personal_information = models.BooleanField(
        default=False, verbose_name="개인정보 동의")
    confirm = models.BooleanField(default=False, verbose_name="확인")

    class Meta:
        verbose_name = '3) 설문지'
        verbose_name_plural = '3) 설문지'


class Application(core_models.TimeStampedModel):
    GENDER_MALE = "GENDER_MALE"
    GENDER_FEMALE = "GENDER_FEMALE"
    GENDER_OTHER = "GENDER_OTHER"
    GENDER_CHOICES = (
        (GENDER_MALE, "남성"),
        (GENDER_FEMALE, "여성"),
        (GENDER_OTHER, "Other"),
    )
    APPROACH_A = "APPROACH_A"
    APPROACH_B = "APPROACH_B"
    APPROACH_C = "APPROACH_C"
    APPROACH_D = "APPROACH_D"
    APPROACH_E = "APPROACH_E"
    APPROACH_F = "APPROACH_F"
    APPROACH_G = "APPROACH_G"
    APPROACH_CHOICES = (
        (APPROACH_A, "지인 소개"),
        (APPROACH_B, "카페, 블로그, 홈페이지"),
        (APPROACH_C, "페이스북, 인스타그램"),
        (APPROACH_D, "유튜브"),
        (APPROACH_E, "책<치유본능> 혹은 <짠맛의 힘>"),
        (APPROACH_F, "외부강연"),
        (APPROACH_G, "제품구입"),
    )
    user = models.OneToOneField(
        "users.User", on_delete=models.PROTECT, verbose_name="회원")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=20, null=True, blank=True, verbose_name="성별"
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name="생년월일")
    address = models.CharField(max_length=2000, verbose_name="주소")
    job = models.CharField(max_length=500, verbose_name="직업")
    phone_number = models.CharField(max_length=500, verbose_name="폰번호")
    email_address = models.CharField(max_length=500, verbose_name="이메일")
    approach = MultiSelectField(
        choices=APPROACH_CHOICES, null=True, blank=True, verbose_name="경로")
    approach_etc = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="경로 기타")
    confirm = models.BooleanField(default=False, verbose_name="확인")

    def get_approach(self):
        return list(self.approach)

    class Meta:
        verbose_name = '4) 신청서'
        verbose_name_plural = '4) 신청서'
