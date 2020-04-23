import graphene
from . import types, queries, mutations


class Query(object):
    me = graphene.Field(types.MeReponse, resolver=queries.resolve_me, required=True)
    get_user = graphene.Field(
        types.GetUserResponse,
        resolver=queries.resolve_get_user,
        required=True,
        args={"uuid": graphene.String(required=True),},
    )
    get_class_users = graphene.Field(
        types.GeClasstUsersResponse,
        resolver=queries.resolve_get_class_users,
        required=True,
        args={"class_order": graphene.Int(required=True),},
    )


class Mutation(object):
    create_user = mutations.CreateUser.Field(required=True)
    update_user = mutations.UpdateUser.Field(required=True)
    remove_user = mutations.RemoveUser.Field(required=True)
