import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class SubmitCheckList(graphene.Mutation):
    class Arguments:
        check_list_cover_uuid = graphene.String(required=True)
        is_previous_answer = graphene.Boolean(required=True)
        true_answer_question_uuids = graphene.List(graphene.String)

    Output = types.SubmitCheckListResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        check_list_cover_uuid = kwargs.get("check_list_cover_uuid")
        is_previous_answer = kwargs.get("is_previous_answer")
        true_answer_question_uuids = kwargs.get("true_answer_question_uuids")
        check_list_cover = models.CheckListCover.objects.get(uuid=check_list_cover_uuid)

        if is_previous_answer:
            all_questions = models.CheckListQuestion.objects.all()
            for question in all_questions:
                models.CheckListAnswer.objects.update_or_create(
                    check_list_cover=check_list_cover,
                    question=question,
                    defaults={"previous_answer": False},
                )
            true_answers = models.CheckListAnswer.objects.filter(
                question__uuid__in=true_answer_question_uuids,
                check_list_cover=check_list_cover,
            )
            true_answers.update(previous_answer=True)
            check_list_cover.previous_submit = True
            check_list_cover.save()
        else:
            all_answers = models.CheckListAnswer.objects.all()
            all_answers.update(later_answer=False)
            true_answers = models.CheckListAnswer.objects.filter(
                question__uuid__in=true_answer_question_uuids,
                check_list_cover=check_list_cover,
            )
            true_answers.update(later_answer=True)
            check_list_cover.later_submit = True
            check_list_cover.save()

        return types.SubmitCheckListResponse(ok=True)
