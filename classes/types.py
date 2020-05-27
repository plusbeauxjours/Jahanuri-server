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


class ApplicationType(DjangoObjectType):
    get_approach = graphene.String(source="get_approach")

    class Meta:
        model = models.Application


class SurveyType(DjangoObjectType):
    class Meta:
        model = models.Survey


class GetClassListReponse(graphene.ObjectType):
    classes = graphene.List(ClassOrderType)


# class CreateClassOrderResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


# class UpdateClassOrderResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


# class RemoveClassOrderResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


class GetReportCoverListResponse(graphene.ObjectType):
    reportCovers = graphene.List(ReportCoverType)


# class CreateReportCoverResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


# class UpdateReportCoverResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


# class RemoveReportCoverResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


class GetReportListResponse(graphene.ObjectType):
    reports = graphene.List(ReportType)


class GetReportDetailResponse(graphene.ObjectType):
    report = graphene.Field(ReportType)


class CreateReportResponse(graphene.ObjectType):
    report = graphene.Field(ReportType)


# class UpdateReportResponse(graphene.ObjectType):
#     report = graphene.Field(ReportType)


# class RemoveReportResponse(graphene.ObjectType):
#     ok = graphene.Boolean()


class SubmitApplicationResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetApplicationResponse(graphene.ObjectType):
    application = graphene.Field(ApplicationType)


class SubmitSurveyResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class GetSurveyResponse(graphene.ObjectType):
    survey = graphene.Field(SurveyType)
