import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from . import models


class CheckListCoverType(DjangoObjectType):
    class Meta:
        model = models.CheckListCover


class CheckListQuestionType(DjangoObjectType):
    class Meta:
        model = models.CheckListQuestion


class CheckListAnswerType(DjangoObjectType):
    class Meta:
        model = models.CheckListAnswer


class CheckListType(graphene.InputObjectType):
    uuid = graphene.String()
    previous = graphene.Boolean()
    later = graphene.Boolean()


class GetCheckListListReponse(graphene.ObjectType):
    checkLists = graphene.List(CheckListAnswerType)


class CheckListResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetCheckListQuestionsResponse(graphene.ObjectType):
    checkListQuestions = graphene.List(CheckListQuestionType)