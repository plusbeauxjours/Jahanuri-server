import uuid
from django.db import models
from users import models as user_models
from core import models as core_models
from multiselectfield import MultiSelectField


class CheckListQuestion(core_models.TimeStampedModel):

    ELEMENT_WOOD = "wood"
    ELEMENT_FIRE = "fire"
    ELEMENT_EARTH = "earth"
    ELEMENT_METAL = "metal"
    ELEMENT_WATER = "water"
    ELEMENT_SANGHWA = "sanghwa"
    ELEMENT_CHOICES = (
        (ELEMENT_WOOD, "Wood"),
        (ELEMENT_FIRE, "Fire"),
        (ELEMENT_EARTH, "Earth"),
        (ELEMENT_METAL, "Metal"),
        (ELEMENT_WATER, "Water"),
        (ELEMENT_SANGHWA, "Sanghwa"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    element = models.CharField(choices=ELEMENT_CHOICES, max_length=20, blank=True)
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
        return self.question.element

    def is_changed(self):
        if self.previous_answer != None and self.later_answer != None:
            return self.previous_answer != self.later_answer

    is_changed.boolean = True


class HabitCheckList(core_models.TimeStampedModel):
    WAKEUP_CONDITION_A = "WAKEUP_CONDITION_A"
    WAKEUP_CONDITION_B = "WAKEUP_CONDITION_B"
    WAKEUP_CONDITION_C = "WAKEUP_CONDITION_C"
    WAKEUP_CONDITION_D = "WAKEUP_CONDITION_D"
    WAKEUP_CONDITION_E = "WAKEUP_CONDITION_E"
    WAKEUP_CONDITION_F = "WAKEUP_CONDITION_F"
    WAKEUP_CONDITION_G = "WAKEUP_CONDITION_G"
    WAKEUP_CONDITION_H = "WAKEUP_CONDITION_H"
    WAKEUP_CONDITION_CHOICES = (
        (WAKEUP_CONDITION_A, "개운하다"),
        (WAKEUP_CONDITION_B, "머리가 아프다"),
        (WAKEUP_CONDITION_C, "눈이 아프거나 잘 안 떠진다"),
        (WAKEUP_CONDITION_D, "몸이 결리거나 뻐근하다"),
        (WAKEUP_CONDITION_E, "일어나기 힘들다"),
        (WAKEUP_CONDITION_F, "멍하다"),
        (WAKEUP_CONDITION_G, "손이나 발 등이 저리다"),
        (WAKEUP_CONDITION_H, "부어있다 (얼굴, 손, 발 등)"),
    )
    WAKEUP_FIRST_THING_A = "WAKEUP_FIRST_THING_A"
    WAKEUP_FIRST_THING_B = "WAKEUP_FIRST_THING_B"
    WAKEUP_FIRST_THING_C = "WAKEUP_FIRST_THING_C"
    WAKEUP_FIRST_THING_D = "WAKEUP_FIRST_THING_D"
    WAKEUP_FIRST_THING_E = "WAKEUP_FIRST_THING_E"
    WAKEUP_FIRST_THING_F = "WAKEUP_FIRST_THING_F"
    WAKEUP_FIRST_THING_CHOICES = (
        (WAKEUP_CONDITION_A, "찬물 혹은 찬음료를 마신다"),
        (WAKEUP_CONDITION_B, "뜨거운 물 혹은 차를 마신다"),
        (WAKEUP_CONDITION_C, "가벼운 스트레칭"),
        (WAKEUP_CONDITION_D, "양치, 세수, 샤워"),
        (WAKEUP_CONDITION_E, "스마트폰"),
        (WAKEUP_CONDITION_F, "잡지, 신문"),
    )
    MEAL_DURING_A = "MEAL_DURING_A"
    MEAL_DURING_B = "MEAL_DURING_B"
    MEAL_DURING_C = "MEAL_DURING_C"
    MEAL_DURING_D = "MEAL_DURING_D"
    MEAL_DURING_E = "MEAL_DURING_E"
    MEAL_DURING_F = "MEAL_DURING_F"
    MEAL_DURING_G = "MEAL_DURING_G"
    MEAL_DURING_H = "MEAL_DURING_H"
    MEAL_DURING_I = "MEAL_DURING_I"
    MEAL_DURING_J = "MEAL_DURING_J"
    MEAL_DURING_K = "MEAL_DURING_K"
    MEAL_DURING_CHOICES = (
        (MEAL_DURING_A, "대화를 많이 하는 편이다"),
        (MEAL_DURING_B, "먹는 것에 집중하는 편이다"),
        (MEAL_DURING_C, "TV, 스마트폰 등을 보면서 먹는다"),
        (MEAL_DURING_D, "꼭꼭 씹어서 먹는다"),
        (MEAL_DURING_E, "급하게 먹는다"),
        (MEAL_DURING_F, "많이 먹는다"),
        (MEAL_DURING_G, "입이 짧다 (많이 못 먹는다)"),
        (MEAL_DURING_H, "음식의 맛을 음미하면서 먹는다"),
        (MEAL_DURING_I, "끼니 때우듯 먹는 편이다"),
        (MEAL_DURING_J, "식욕이 별로 없다"),
        (MEAL_DURING_K, "밥맛이 아주 좋다"),
    )
    DEGREE_A = "DEGREE_A"
    DEGREE_B = "DEGREE_B"
    DEGREE_C = "DEGREE_C"
    DEGREE_D = "DEGREE_D"
    DEGREE_E = "DEGREE_E"
    DEGREE_CHOICES = (
        (DEGREE_A, "안한다"),
        (DEGREE_B, "거의 안한다"),
        (DEGREE_C, "가끔 한다"),
        (DEGREE_D, "거의 한다"),
        (DEGREE_E, "자주 한다"),
    )
    AFTER_LUNCH_A = "AFTER_LUNCH_A"
    AFTER_LUNCH_B = "AFTER_LUNCH_B"
    AFTER_LUNCH_C = "AFTER_LUNCH_C"
    AFTER_LUNCH_D = "AFTER_LUNCH_D"
    AFTER_LUNCH_E = "AFTER_LUNCH_E"
    AFTER_LUNCH_F = "AFTER_LUNCH_F"
    AFTER_LUNCH_CHOICES = (
        (AFTER_LUNCH_A, "스마트폰을 본다"),
        (AFTER_LUNCH_B, "밖에 나가 걷거나 산책을 한다"),
        (AFTER_LUNCH_C, "담배를 핀다"),
        (AFTER_LUNCH_D, "커피 등 후식을 즐긴다"),
        (AFTER_LUNCH_E, "수다를 즐긴다"),
        (AFTER_LUNCH_F, "잠이 쏟아진다"),
    )
    SAYING_A = "SAYING_A"
    SAYING_B = "SAYING_B"
    SAYING_C = "SAYING_C"
    SAYING_D = "SAYING_D"
    SAYING_E = "SAYING_E"
    SAYING_F = "SAYING_F"
    SAYING_G = "SAYING_G"
    SAYING_H = "SAYING_H"
    SAYING_I = "SAYING_I"
    SAYING_J = "SAYING_J"
    SAYING_K = "SAYING_K"
    SAYING_CHOICES = (
        (SAYING_A, "말의 속도가 빠르다"),
        (SAYING_B, "듣는 것보다 말하는 것에 더 익숙하다"),
        (SAYING_C, "상대방의 말을 잘 듣는 편이다"),
        (SAYING_D, "말을 자주 더듬는다"),
        (SAYING_E, "말을 거침없이 한다"),
        (SAYING_F, "자주 흥분해서 말한다"),
        (SAYING_G, "말이 별로 없다"),
        (SAYING_H, "생각을 하고 말을 하는 편이다"),
        (SAYING_I, "말을 하면서 생각하는 편이다"),
        (SAYING_J, "말실수를 많이 한다"),
        (SAYING_K, "부정적인 반응을 자주 보인다(아닌 것 같은데~ 등)"),
    )
    WALKING_A = "WALKING_A"
    WALKING_B = "WALKING_B"
    WALKING_C = "WALKING_C"
    WALKING_D = "WALKING_D"
    WALKING_E = "WALKING_E"
    WALKING_F = "WALKING_F"
    WALKING_G = "WALKING_G"
    WALKING_H = "WALKING_H"
    WALKING_CHOICES = (
        (WALKING_A, "걸음이 느리다"),
        (WALKING_B, "걸음이 빠른 편이다"),
        (WALKING_C, "옆사람과 나란히 걷는다"),
        (WALKING_D, "앞서서 걷는 편이다"),
        (WALKING_E, "발을 끌면서 걷는다"),
        (WALKING_F, "허리가 굽어 있다"),
        (WALKING_G, "파워워킹을 한다"),
        (WALKING_H, "오래 걷지 못한다"),
    )
    POSTURE_A = "POSTURE_A"
    POSTURE_B = "POSTURE_B"
    POSTURE_C = "POSTURE_C"
    POSTURE_D = "POSTURE_D"
    POSTURE_E = "POSTURE_E"
    POSTURE_CHOICES = (
        (POSTURE_A, "앉아 있는 시간"),
        (POSTURE_B, "서 있는 시간"),
        (POSTURE_C, "걷는 시간"),
        (POSTURE_D, "교통수단을 이용하는 시간"),
        (POSTURE_E, "누워 있는 시간"),
    )
    POSTURE_DETAIL_A = "POSTURE_DETAIL_A"
    POSTURE_DETAIL_B = "POSTURE_DETAIL_B"
    POSTURE_DETAIL_C = "POSTURE_DETAIL_C"
    POSTURE_DETAIL_D = "POSTURE_DETAIL_D"
    POSTURE_DETAIL_E = "POSTURE_DETAIL_E"
    POSTURE_DETAIL_F = "POSTURE_DETAIL_F"
    POSTURE_DETAIL_G = "POSTURE_DETAIL_G"
    POSTURE_DETAIL_H = "POSTURE_DETAIL_H"
    POSTURE_DETAIL_I = "POSTURE_DETAIL_I"
    POSTURE_DETAIL_J = "POSTURE_DETAIL_J"
    POSTURE_DETAIL_CHOICES = (
        (POSTURE_DETAIL_A, "자세를 편하게 잘 펴고 있다"),
        (POSTURE_DETAIL_B, "자세가 무너져 있다"),
        (POSTURE_DETAIL_C, "앉아 있는 것에 익숙하다"),
        (POSTURE_DETAIL_D, "오래 서 있지 못한다"),
        (POSTURE_DETAIL_E, "앉아 있는 게 힘들다"),
        (POSTURE_DETAIL_F, "등이 굽어 있거나 거북목이다"),
        (POSTURE_DETAIL_G, "일자목, 목이 돌아가지 않는다"),
        (POSTURE_DETAIL_H, "다리를 자주 꼰다"),
        (POSTURE_DETAIL_I, "무지외반증이 있다"),
        (POSTURE_DETAIL_J, "다리가 휘어 있다 (안으로, 밖으로 등)"),
    )
    BODY_HEAT_A = "BODY_HEAT_A"
    BODY_HEAT_B = "BODY_HEAT_B"
    BODY_HEAT_C = "BODY_HEAT_C"
    BODY_HEAT_D = "BODY_HEAT_D"
    BODY_HEAT_E = "BODY_HEAT_E"
    BODY_HEAT_F = "BODY_HEAT_F"
    BODY_HEAT_G = "BODY_HEAT_G"
    BODY_HEAT_H = "BODY_HEAT_H"
    BODY_HEAT_I = "BODY_HEAT_I"
    BODY_HEAT_J = "BODY_HEAT_J"
    BODY_HEAT_K = "BODY_HEAT_K"
    BODY_HEAT_CHOICES = (
        (BODY_HEAT_A, "열이 많아서 옷을 얇게 입는다"),
        (BODY_HEAT_B, "찬물을 피한다"),
        (BODY_HEAT_C, "찬물을 즐겨 마신다"),
        (BODY_HEAT_D, "뜨거운 차를 자주 마신다"),
        (BODY_HEAT_E, "핫팩을 자주 붙이고 다닌다"),
        (BODY_HEAT_F, "목도리, 장갑 등을 챙겨서 한다"),
        (BODY_HEAT_G, "내의를 챙겨 입는다"),
        (BODY_HEAT_H, "발을 항상 따듯하게 해 준다"),
        (BODY_HEAT_I, "발이 답답해서 집에서 맨발로 다닌다"),
        (BODY_HEAT_J, "찜질팩, 돌뜸 등을 늘 챙겨서 한다"),
        (BODY_HEAT_K, "족탕, 반신욕, 찜질 등을 한다"),
    )
    SLEEPING_A = "SLEEPING_A"
    SLEEPING_B = "SLEEPING_B"
    SLEEPING_C = "SLEEPING_C"
    SLEEPING_D = "SLEEPING_D"
    SLEEPING_CHOICES = (
        (SLEEPING_A, "머리를 대면 바로 잠든다"),
        (SLEEPING_B, "한참을 뒤척이다 자야 한다"),
        (SLEEPING_C, "새벽에 꼭 한 번(이상) 일어난다"),
        (SLEEPING_D, "잠을 못 잔다"),
    )
    BEFORE_SLEEPING_A = "BEFORE_SLEEPING_A"
    BEFORE_SLEEPING_B = "BEFORE_SLEEPING_B"
    BEFORE_SLEEPING_C = "BEFORE_SLEEPING_C"
    BEFORE_SLEEPING_D = "BEFORE_SLEEPING_D"
    BEFORE_SLEEPING_E = "BEFORE_SLEEPING_E"
    BEFORE_SLEEPING_CHOICES = (
        (BEFORE_SLEEPING_A, "스마트폰"),
        (BEFORE_SLEEPING_B, "TV시청"),
        (BEFORE_SLEEPING_C, "책, 잡지, 신문 등 읽기"),
        (BEFORE_SLEEPING_D, "일기, 글쓰기"),
        (BEFORE_SLEEPING_E, "야식"),
    )

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    wakeup_time = models.CharField(max_length=200)
    wakeup_long = models.CharField(max_length=200)
    wakeup_condition = MultiSelectField(
        choices=WAKEUP_CONDITION_CHOICES, null=True, blank=True
    )
    wakeup_condition_etc = models.CharField(max_length=2000, null=True, blank=True)
    wakeup_first_thing = MultiSelectField(
        choices=WAKEUP_FIRST_THING_CHOICES, null=True, blank=True
    )
    wakeup_first_thing_etc = models.CharField(max_length=2000, null=True, blank=True)
    meal = models.CharField(max_length=3000, null=True, blank=True)
    meal_during = MultiSelectField(choices=MEAL_DURING_CHOICES, null=True, blank=True)
    meal_during_etc = models.CharField(max_length=2000, null=True, blank=True)
    meal_with_water = models.CharField(
        choices=DEGREE_CHOICES, max_length=300, null=True, blank=True
    )
    meal_with_snack = models.CharField(
        choices=DEGREE_CHOICES, max_length=300, null=True, blank=True
    )
    meal_with_night_food = models.CharField(
        choices=DEGREE_CHOICES, max_length=300, null=True, blank=True
    )
    after_lunch = MultiSelectField(choices=AFTER_LUNCH_CHOICES, null=True, blank=True)
    after_lunch_etc = models.CharField(max_length=2000, null=True, blank=True)
    saying = MultiSelectField(choices=SAYING_CHOICES, null=True, blank=True)
    saying_etc = models.CharField(max_length=2000, null=True, blank=True)
    saying_repeat = models.CharField(max_length=2000)
    walking = MultiSelectField(choices=WALKING_CHOICES, null=True, blank=True)
    walking_etc = models.CharField(max_length=2000, null=True, blank=True)
    posture = MultiSelectField(choices=POSTURE_CHOICES, null=True, blank=True)
    posture_etc = models.CharField(max_length=2000, null=True, blank=True)
    posture_detail = MultiSelectField(
        choices=POSTURE_DETAIL_CHOICES, null=True, blank=True
    )
    posture_detail_etc = models.CharField(max_length=2000, null=True, blank=True)
    body_heat = MultiSelectField(choices=BODY_HEAT_CHOICES, null=True, blank=True)
    body_heat_etc = models.CharField(max_length=2000, null=True, blank=True)
    exercise = models.CharField(max_length=2000)
    sleeping = MultiSelectField(choices=SLEEPING_CHOICES, null=True, blank=True)
    sleeping_etc = models.CharField(max_length=2000, null=True, blank=True)
    before_sleeping = MultiSelectField(
        choices=BEFORE_SLEEPING_CHOICES, null=True, blank=True
    )
    before_sleeping_etc = models.CharField(max_length=2000, null=True, blank=True)
    good_thing = models.CharField(max_length=2000)
    bad_thing = models.CharField(max_length=2000)
