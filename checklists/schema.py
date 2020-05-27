import graphene
from . import types, queries, mutations


class Query(object):
    get_check_list_questions = graphene.Field(
        types.GetCheckListQuestionsResponse,
        resolver=queries.resolve_get_check_list_questions,
        required=True,
    )
    get_habit_check_list = graphene.Field(
        types.GetHabitCheckListResponse,
        resolver=queries.resolve_get_habit_check_list,
        required=True,
    )


class Mutation(object):
    submit_check_list = mutations.SubmitCheckList.Field(required=True)
    submit_habit_check_list = mutations.SubmitHabitCheckList.Field(required=True)
