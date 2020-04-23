import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from . import models


class ClassOrderType(DjangoObjectType):
    class Meta:
        model = models.ClassOrder


class ReportCoverType(DjangoObjectType):
    class Meta:
        model = models.ReportCover


class ReportType(DjangoObjectType):
    class Meta:
        model = models.Report


class GetAllClassesReponse(graphene.ObjectType):
    clasees = graphene.List(ClassOrderType)


class CreateClassOrderResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class UpdateClassOrderResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class RemoveClassOrderResponse(graphene.ObjectType):
    ok = graphene.Boolean()
