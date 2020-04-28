import uuid
from django.db import models
from users import models as user_models
from core import models as core_models


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
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    question = models.ForeignKey(
        CheckListQuestion, on_delete=models.CASCADE, related_name="question_set"
    )
    previous_answer = models.BooleanField(default=False)
    later_answer = models.BooleanField(default=False)

    def element(self):
        return self.question.elements

    def is_changed(self):
        if self.previous_answer != None and self.later_answer != None:
            return self.previous_answer != self.later_answer

    is_changed.boolean = True
