import graphene
from . import types, queries, mutations


class Query(object):
    get_feed_list = graphene.Field(
        types.GetFeedListResponse,
        resolver=queries.resolve_get_feed_list,
        required=True,
    )
    get_feed_list_staff = graphene.Field(
        types.GetFeedListStaffResponse,
        resolver=queries.resolve_get_feed_list_staff,
        required=True,
        args={"class_order_uuid": graphene.String(required=True),},
    )


class Mutation(object):
    create_feed = mutations.CreateFeed.Field(required=True)
    remove_feed = mutations.RemoveFeed.Field(required=True)
