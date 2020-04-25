import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class CheckList(graphene.Mutation):
    class Arguments:
        check_list_cover_uuid = graphene.String(required=True)
        check_list_set = graphene.List(types.CheckListType)

    Output = types.CheckListResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        check_list_cover_uuid = kwargs.get("check_list_cover_uuid")
        check_list_set = kwargs.get("check_list_set")
        check_list_cover = models.CheckListCover.objects.get(uuid=check_list_cover_uuid)
        for cl in check_list_set:
            question = models.CheckListQuestion.objects.get(uuid=cl.uuid)
            check_list, created = models.CheckListAnswer.objects.get_or_create(
                check_list_cover=check_list_cover, question=question,
            )
            check_list.previous_answer = cl.previous
            check_list.later_answer = cl.later
            check_list.save()

        return types.CheckListResponse(ok=True)

