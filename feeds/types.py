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
    ok = graphene.Boolean()


class RemoveFeedReponse(graphene.ObjectType):
    ok = graphene.Boolean()
