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


class GetClassListReponse(graphene.ObjectType):
    clasees = graphene.List(ClassOrderType)


class CreateClassOrderResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class UpdateClassOrderResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class RemoveClassOrderResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetReportCoverListResponse(graphene.ObjectType):
    reportCovers = graphene.List(ReportCoverType)


class CreateReportCoverResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class UpdateReportCoverResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class RemoveReportCoverResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetReportListResponse(graphene.ObjectType):
    reports = graphene.List(ReportType)


# class CreateReportResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


# class UpdateReportResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


# class RemoveReportResponse(graphene.ObjectType):
#     ok = graphene.Boolean()
