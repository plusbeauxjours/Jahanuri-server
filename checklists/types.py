import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from . import models


class CheckListQuestionType(DjangoObjectType):
    class Meta:
        model = models.CheckListQuestion


class CheckListAnswerType(DjangoObjectType):
    class Meta:
        model = models.CheckListAnswer


class HabitCheckListType(DjangoObjectType):
    get_wakeup_condition = graphene.String(source="get_wakeup_condition")
    get_wakeup_first_thing = graphene.String(source="get_wakeup_first_thing")
    get_meal_during = graphene.String(source="get_meal_during")
    get_after_lunch = graphene.String(source="get_after_lunch")
    get_saying = graphene.String(source="get_saying")
    get_walking = graphene.String(source="get_walking")
    get_posture = graphene.String(source="get_posture")
    get_posture_detail = graphene.String(source="get_posture_detail")
    get_body_heat = graphene.String(source="get_body_heat")
    get_sleeping = graphene.String(source="get_sleeping")
    get_before_sleeping = graphene.String(source="get_before_sleeping")

    class Meta:
        model = models.HabitCheckList


class SubmitCheckListResponse(graphene.ObjectType):
    checkListQuestions = graphene.List(CheckListQuestionType)


class SubmitHabitCheckListResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class CheckListSubmitResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetCheckListQuestionsResponse(graphene.ObjectType):
    checkListQuestions = graphene.List(CheckListQuestionType)


class GetHabitCheckListResponse(graphene.ObjectType):
    habitCheckList = graphene.Field(HabitCheckListType)
