import graphene
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from . import models


class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class MeReponse(graphene.ObjectType):
    user = graphene.Field(UserType)
