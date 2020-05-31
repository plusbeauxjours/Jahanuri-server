import graphene
from graphene_django.types import DjangoObjectType
from . import models
from users import types as user_types


class FeedType(DjangoObjectType):
    class Meta:
        model = models.Feed


class GetFeedListResponse(graphene.ObjectType):
    feeds = graphene.List(FeedType)


class GetFeedListStaffResponse(graphene.ObjectType):
    feeds = graphene.List(FeedType)


class CreateFeedReponse(graphene.ObjectType):
    feed = graphene.Field(FeedType)
    users = graphene.List(user_types.UserType)


class RemoveFeedReponse(graphene.ObjectType):
    uuid = graphene.String()
