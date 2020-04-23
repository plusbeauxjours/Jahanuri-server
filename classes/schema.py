import graphene
from . import types, queries, mutations


class Query(object):
    get_all_classes = graphene.Field(
        types.GetAllClassesReponse,
        resolver=queries.resolve_get_all_classes,
        required=True,
    )


class Mutation(object):
    create_class_order = mutations.CreateClassOrder.Field(required=True)
    update_class_order = mutations.UpdateClassOrder.Field(required=True)
    remove_class_order = mutations.RemoveClassOrder.Field(required=True)
