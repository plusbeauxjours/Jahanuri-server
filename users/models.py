from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from core import models as core_models
from checklists import models as check_list_models
from multiselectfield import MultiSelectField


class User(AbstractUser):
    GENDER_MALE = "GENDER_MALE"
    GENDER_FEMALE = "GENDER_FEMALE"
    GENDER_OTHER = "GENDER_OTHER"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user_img = models.ImageField(upload_to="user_imgs/", null=True, blank=True)
    class_order = models.ForeignKey(
        "classes.ClassOrder", on_delete=models.PROTECT, blank=True, null=True
    )
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=20, null=True, blank=True
    )
    birth_date = models.DateField()
    address = models.CharField(max_length=2000)
    job = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    email_address = models.CharField(max_length=500)
    approach = MultiSelectField(choices=APPROACH_CHOICES, null=True, blank=True)
    approach_etc = models.CharField(max_length=2000, null=True, blank=True)
    has_submitted_previous_check_list = models.BooleanField(default=False)
    has_submitted_later_check_list = models.BooleanField(default=False)
    has_submitted_habit_check_list = models.BooleanField(default=False)
    has_submitted_application = models.BooleanField(default=False)
    has_submitted_survey = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)
    has_kakao_account = models.BooleanField(default=False)
    has_apple_account = models.BooleanField(default=False)

    def wood_before(self):
        wood = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="wood", previous_answer=True
        )
        return wood.count()

    def wood_after(self):
        wood = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="wood", later_answer=True
        )
        return wood.count()

    def fire_before(self):
        fire = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="fire", previous_answer=True
        )
        return fire.count()

    def fire_after(self):
        fire = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="fire", later_answer=True
        )
        return fire.count()

    def earth_before(self):
        earth = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="earth", previous_answer=True
        )
        return earth.count()

    def earth_after(self):
        earth = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="earth", later_answer=True
        )
        return earth.count()

    def metal_before(self):
        metal = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="metal", previous_answer=True
        )
        return metal.count()

    def metal_after(self):
        metal = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="metal", later_answer=True
        )
        return metal.count()

    def water_before(self):
        water = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="water", previous_answer=True
        )
        return water.count()

    def water_after(self):
        water = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="water", later_answer=True
        )
        return water.count()

    def sanghwa_before(self):
        sanghwa = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="sanghwa", previous_answer=True
        )
        return sanghwa.count()

    def sanghwa_after(self):
        sanghwa = check_list_models.CheckListAnswer.objects.filter(
            user=self, question__element="sanghwa", later_answer=True
        )
        return sanghwa.count()

    def __str__(self):
        return self.username
