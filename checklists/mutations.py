import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class SubmitCheckList(graphene.Mutation):
    class Arguments:
        is_previous_answer = graphene.Boolean(required=True)
        true_answer_question_uuids = graphene.List(graphene.String)

    Output = types.SubmitCheckListResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        is_previous_answer = kwargs.get("is_previous_answer")
        true_answer_question_uuids = kwargs.get("true_answer_question_uuids")
        if is_previous_answer:
            all_questions = models.CheckListQuestion.objects.all()
            for question in all_questions:
                models.CheckListAnswer.objects.update_or_create(
                    user=user, question=question, defaults={"previous_answer": False,},
                )
            true_answers = models.CheckListAnswer.objects.filter(
                question__uuid__in=true_answer_question_uuids, user=user,
            )
            true_answers.update(previous_answer=True)
            user.has_previous_check_list_submitted = True
            user.save()
            return types.SubmitCheckListResponse(ok=True)

        else:
            all_answers = models.CheckListAnswer.objects.all()
            all_answers.update(later_answer=False)
            true_answers = models.CheckListAnswer.objects.filter(
                question__uuid__in=true_answer_question_uuids, user=user,
            )
            true_answers.update(later_answer=True)
            user.has_later_check_list_submitted = True
            user.save()
            return types.SubmitCheckListResponse(ok=True)
