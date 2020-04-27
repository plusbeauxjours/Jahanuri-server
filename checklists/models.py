import uuid
from django.db import models
from users import models as user_models
from core import models as core_models


class CheckListCover(core_models.TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    previous_submit = models.BooleanField(default=False)
    later_submit = models.BooleanField(default=False)

    def wood_before(self):
        wood = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="wood", previous_answer=True
        )
        return wood.count()

    def wood_after(self):
        wood = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="wood", later_answer=True
        )
        return wood.count()

    def fire_before(self):
        fire = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="fire", previous_answer=True
        )
        return fire.count()

    def fire_after(self):
        fire = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="fire", later_answer=True
        )
        return fire.count()

    def earth_before(self):
        earth = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="earth", previous_answer=True
        )
        return earth.count()

    def earth_after(self):
        earth = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="earth", later_answer=True
        )
        return earth.count()

    def metal_before(self):
        metal = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="metal", previous_answer=True
        )
        return metal.count()

    def metal_after(self):
        metal = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="metal", later_answer=True
        )
        return metal.count()

    def water_before(self):
        water = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="water", previous_answer=True
        )
        return water.count()

    def water_after(self):
        water = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="water", later_answer=True
        )
        return water.count()

    def sanghwa_before(self):
        sanghwa = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="sanghwa", previous_answer=True
        )
        return sanghwa.count()

    def sanghwa_after(self):
        sanghwa = CheckListAnswer.objects.filter(
            check_list_cover=self, question__elements="sanghwa", later_answer=True
        )
        return sanghwa.count()


    def __str__(self):
        return self.user.username


class CheckListQuestion(core_models.TimeStampedModel):

    ELEMENTS_WOOD = "wood"
    ELEMENTS_FIRE = "fire"
    ELEMENTS_EARTH = "earth"
    ELEMENTS_METAL = "metal"
    ELEMENTS_WATER = "water"
    ELEMENTS_SANGHWA = "sanghwa"
    ELEMENTS_CHOICES = (
        (ELEMENTS_WOOD, "Wood"),
        (ELEMENTS_FIRE, "Fire"),
        (ELEMENTS_EARTH, "Earth"),
        (ELEMENTS_METAL, "Metal"),
        (ELEMENTS_WATER, "Water"),
        (ELEMENTS_SANGHWA, "Sanghwa"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    elements = models.CharField(choices=ELEMENTS_CHOICES, max_length=20, blank=True)
    question = models.CharField(max_length=5000)

    def __str__(self):
        return self.question


class CheckListAnswer(core_models.TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    check_list_cover = models.ForeignKey(CheckListCover, on_delete=models.CASCADE)
    question = models.ForeignKey(
        CheckListQuestion, on_delete=models.CASCADE, related_name="question_set"
    )
    previous_answer = models.BooleanField(blank=True, null=True)
    later_answer = models.BooleanField(blank=True, null=True)


    def element(self):
        return self.question.elements

    def is_changed(self):
        if self.previous_answer != None and self.later_answer != None:
            return self.previous_answer != self.later_answer

    is_changed.boolean = True
