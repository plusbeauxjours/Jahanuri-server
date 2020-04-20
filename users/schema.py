import graphene
from . import types, queries, mutations


class Query(object):
    me = graphene.Field(types.MeReponse, resolver=queries.resolve_me, required=True)


class Mutation(object):
    pass
