import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from . import models


class ClassOrderType(DjangoObjectType):
    class Meta:
        model = models.ClassOrder


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


class GetSurveyListResponse(graphene.ObjectType):
    surveys = graphene.List(SurveyType)


class GetSurveyDetailResponse(graphene.ObjectType):
    survey = graphene.Field(SurveyType)
