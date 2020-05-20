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
    checkListQuestions = graphene.List(CheckListQuestionType)


class CheckListSubmitResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetCheckListQuestionsResponse(graphene.ObjectType):
    checkListQuestions = graphene.List(CheckListQuestionType)

