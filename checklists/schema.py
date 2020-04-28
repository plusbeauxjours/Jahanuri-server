import graphene
from . import types, queries, mutations


class Query(object):
    get_check_list_answers = graphene.Field(
        types.GetCheckListAnswersResponse,
        resolver=queries.resolve_get_check_list_answers,
        required=True,
    )


class Mutation(object):
    submit_check_list = mutations.SubmitCheckList.Field(required=True)
