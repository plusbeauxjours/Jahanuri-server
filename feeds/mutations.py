import graphene
from graphql_jwt.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from classes import models as class_models
from users import models as user_models
from . import types, models


class CreateFeed(graphene.Mutation):
    class Arguments:
        class_order_uuid = graphene.String(required=True)
        text = graphene.String(required=True)

    Output = types.CreateFeedReponse

    def mutate(self, info, **kwargs):
        user = info.context.user
        class_order_uuid = kwargs.get("class_order_uuid")
        text = kwargs.get("text")
        class_order = class_models.ClassOrder.objects.get(
            uuid=class_order_uuid)
        class_user = user_models.User.objects.filter(class_order=class_order)
        new_feed = models.Feed.objects.create(
            user=user, text=text, class_order=class_order
        )

        return types.CreateFeedReponse(feed=new_feed, users=class_user)


class RemoveFeed(graphene.Mutation):
    class Arguments:
        feed_uuid = graphene.String(required=True)

    Output = types.RemoveFeedReponse

    def mutate(self, info, **kwargs):
        feed_uuid = kwargs.get("feed_uuid")
        feed = models.Feed.objects.get(uuid=feed_uuid)
        feed.delete()

        return types.RemoveFeedReponse(uuid=feed_uuid)
