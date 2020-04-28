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


class SubmitCheckListResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class CheckListSubmitResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetCheckListAnswersResponse(graphene.ObjectType):
    checkListAnswers = graphene.List(CheckListAnswerType)
