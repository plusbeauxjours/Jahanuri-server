from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from core import models as core_models
from checklists import models as check_list_models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    user_img = models.ImageField(upload_to="user_imgs/", null=True, blank=True)
    bio = models.TextField(blank=True)
    class_order = models.ForeignKey(
        "classes.ClassOrder", on_delete=models.PROTECT, blank=True, null=True
    )
    has_previous_check_list_submitted = models.BooleanField(default=False)
    has_later_check_list_submitted = models.BooleanField(default=False)
    has_submited_application = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)
    has_kakao_account = models.BooleanField(default=False)

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
