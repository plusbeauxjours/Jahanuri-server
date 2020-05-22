import graphene
from graphene_django.types import DjangoObjectType
from . import models


class FeedType(DjangoObjectType):
    class Meta:
        model = models.Feed


class GetFeedListResponse(graphene.ObjectType):
    feeds = graphene.List(FeedType)


class GetFeedListStaffResponse(graphene.ObjectType):
    feeds = graphene.List(FeedType)


class CreateFeedReponse(graphene.ObjectType):
    feed = graphene.Field(FeedType)


class RemoveFeedReponse(graphene.ObjectType):
    uuid = graphene.String()
