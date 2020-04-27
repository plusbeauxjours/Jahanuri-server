import graphene
from . import types, queries, mutations


class Query(object):
    get_check_list_list = graphene.Field(
        types.GetCheckListListReponse,
        resolver=queries.resolve_get_check_list_list,
        required=True,
        args={"user_uuid": graphene.String(), "name": graphene.String()},
    )
    get_check_list_questions = graphene.Field(
        types.GetCheckListQuestionsResponse,
        resolver=queries.resolve_get_check_list_questions,
        required=True,
    )


class Mutation(object):
    check_list = mutations.CheckList.Field(required=True)
