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
