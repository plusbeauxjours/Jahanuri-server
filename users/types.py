import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from classes import models as class_models
from . import models


class UserType(DjangoObjectType):
    report_cover_uuid = graphene.String()

    def resolve_report_cover_uuid(self, info):
        user = info.context.user
        try:
            report_cover = class_models.ReportCover.objects.get(
                user=user, report_type="BODY_STUDY"
            )
            return report_cover.uuid
        except:
            return

    class Meta:
        model = models.User


class MeReponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class GetUserResponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class GetClasstUsersResponse(graphene.ObjectType):
    users = graphene.List(UserType)


class GetUserListResponse(graphene.ObjectType):
    users = graphene.List(UserType)


class CreateUserResponse(graphene.ObjectType):
    ok = graphene.Boolean()
    user = graphene.Field(UserType)


class UpdateUserResponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class RemoveUserResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class AppleConnectResponse(graphene.ObjectType):
    ok = graphene.Boolean()
    token = graphene.String()
