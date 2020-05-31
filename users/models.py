from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from core import models as core_models
from classes import models as class_models
from checklists import models as check_list_models
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
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
    APPROACH_CHOICES = (
        (APPROACH_A, "지인 소개"),
        (APPROACH_B, "카페, 블로그"),
        (APPROACH_C, "페이스북, 트위터"),
        (APPROACH_D, "책 <치유본능>"),
        (APPROACH_E, "책 <짠맛의 힘>"),
        (APPROACH_F, "홈페이지(자하누리, 직관의 몸공부)"),
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="고유 번호")
    class_order = models.ForeignKey(
        "classes.ClassOrder", on_delete=models.PROTECT, blank=True, null=True, verbose_name="기수"
    )
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=20, null=True, blank=True, verbose_name="성별"
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name="생년월일")
    address = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="주소")
    job = models.CharField(max_length=500, null=True,
                           blank=True, verbose_name="직업")
    phone_number = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="폰번호")
    approach = MultiSelectField(
        choices=APPROACH_CHOICES, null=True, blank=True, verbose_name="경로")
    approach_etc = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="경로 기타")
    has_married = models.BooleanField(default=False, verbose_name="결혼")
    has_married_etc = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="결혼 기타")
    has_childbirth = models.BooleanField(default=False, verbose_name="출산")
    has_childbirth_etc = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="출산 기타")
    has_submitted_previous_check_list = models.BooleanField(
        default=False, verbose_name="체크 1")
    has_submitted_later_check_list = models.BooleanField(
        default=False, verbose_name="체크 2")
    has_submitted_habit_check_list = models.BooleanField(
        default=False, verbose_name="습관")
    has_submitted_application = models.BooleanField(
        default=False, verbose_name="신청서")
    has_submitted_survey = models.BooleanField(
        default=False, verbose_name="설문지")
    has_paid = models.BooleanField(default=False, verbose_name="결제")
    has_apple_account = models.BooleanField(
        default=False, verbose_name="애플 로긴")
    apple_id = models.CharField(
        blank=True, null=True, max_length=80, verbose_name="애플 아뒤")
    push_token = models.CharField(
        blank=True, null=True, max_length=200, verbose_name="푸쉬 토큰")

    def wood_before(self):
        wood = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_WOOD", previous_answer=True
        )
        return wood.count()

    def wood_after(self):
        wood = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_WOOD", later_answer=True
        )
        return wood.count()

    def fire_before(self):
        fire = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_FIRE", previous_answer=True
        )
        return fire.count()

    def fire_after(self):
        fire = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_FIRE", later_answer=True
        )
        return fire.count()

    def earth_before(self):
        earth = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_EARTH", previous_answer=True
        )
        return earth.count()

    def earth_after(self):
        earth = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_EARTH", later_answer=True
        )
        return earth.count()

    def metal_before(self):
        metal = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_METAL", previous_answer=True
        )
        return metal.count()

    def metal_after(self):
        metal = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_METAL", later_answer=True
        )
        return metal.count()

    def water_before(self):
        water = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_WATER", previous_answer=True
        )
        return water.count()

    def water_after(self):
        water = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_WATER", later_answer=True
        )
        return water.count()

    def sanghwa_before(self):
        sanghwa = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_SANGHWA", previous_answer=True
        )
        return sanghwa.count()

    def sanghwa_after(self):
        sanghwa = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="ELEMENT_SANGHWA", later_answer=True
        )
        return sanghwa.count()

    def __str__(self):
        return self.username

    wood_before.short_description = '목 1'
    wood_after.short_description = '목 2'
    fire_before.short_description = '화 1'
    fire_after.short_description = '화 2'
    earth_before.short_description = '토 1'
    earth_after.short_description = '토 2'
    metal_before.short_description = '금 1'
    metal_after.short_description = '금 2'
    water_before.short_description = '수 1'
    water_after.short_description = '수 2'
    sanghwa_before.short_description = '상화 1'
    sanghwa_after.short_description = '상화 2'


@receiver(post_save, sender=User)
def do_something_when_user_paid(sender, instance, created, **kwargs):
    if not created:
        user = instance
        if user.has_paid == True and user.class_order == None:
            class_order = class_models.ClassOrder.objects.last()
            user.class_order = class_order
            user.save()
