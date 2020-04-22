import graphene
from . import types, queries, mutations


class Query(object):
    me = graphene.Field(types.MeReponse, resolver=queries.resolve_me, required=True)


class Mutation(object):
    me_mutation = mutations.MeMutation.Field(required=True)
    create_user = mutations.CreateUser.Field(required=True)
    update_user = mutations.UpdateUser.Field(required=True)
