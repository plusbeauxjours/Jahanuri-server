from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    user_img = models.ImageField(upload_to="user_imgs/", null=True, blank=True)
    bio = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
