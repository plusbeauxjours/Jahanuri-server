import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from . import models


class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class MeReponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class GetUserResponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class GeClasstUsersResponse(graphene.ObjectType):
    users = graphene.List(UserType)


class CreateUserResponse(graphene.ObjectType):
    ok = graphene.Boolean()
    user = graphene.Field(UserType)


class UpdateUserResponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class RemoveUserResponse(graphene.ObjectType):
    ok = graphene.Boolean()
