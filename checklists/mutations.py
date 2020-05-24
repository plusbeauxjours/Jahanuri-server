import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class SubmitHabitCheckList(graphene.Mutation):
    class Arguments:
        user_uuid = graphene.String(required=True)
        job = graphene.String(required=True)
        wakeup_time = graphene.String(required=True)
        wakeup_long = graphene.String(required=True)
        wakeup_condition = graphene.List(graphene.String)
        wakeup_condition_etc = graphene.String()
        wakeup_first_thing = graphene.List(graphene.String)
        wakeup_first_thing_etc = graphene.String()
        meal = graphene.String()
        meal_during = graphene.List(graphene.String)
        meal_during_etc = graphene.String()
        meal_with_water = graphene.List(graphene.String)
        meal_with_snack = graphene.List(graphene.String)
        meal_with_night_food = graphene.List(graphene.String)
        after_lunch = graphene.List(graphene.String)
        after_lunch_etc = graphene.String()
        saying = graphene.List(graphene.String)
        saying_etc = graphene.String()

    Output = types.SubmitHabitCheckListResponse

    @login_required
    def mutate(self, info, **kwargs):
        user_uuid = kwargs.get("user_uuid")
        job = kwargs.get("job")
        wakeup_time = kwargs.get("wakeup_time")
        wakeup_long = kwargs.get("wakeup_long")
        wakeup_condition = kwargs.get("wakeup_condition")
        wakeup_condition_etc = kwargs.get("wakeup_condition_etc")
        wakeup_first_thing = kwargs.get("wakeup_first_thing")
        wakeup_first_thing_etc = kwargs.get("wakeup_first_thing_etc")
        meal = kwargs.get("meal")
        meal_during = kwargs.get("meal_during")
        meal_during_etc = kwargs.get("meal_during_etc")
        meal_with_water = kwargs.get("meal_with_water")
        meal_with_snack = kwargs.get("meal_with_snack")
        meal_with_night_food = kwargs.get("meal_with_night_food")
        after_lunch = kwargs.get("after_lunch")
        after_lunch_etc = kwargs.get("after_lunch_etc")
        saying = kwargs.get("saying")
        saying_etc = kwargs.get("saying_etc")
        # @login_required
        # def mutate(self, info, **kwargs):
        #     user = info.context.user
        #     models.HabitCheckList.objects.create(
        #         user=user,
        #         job="백수",
        #         wakeup_time="아침 두시",
        #         wakeup_long="3시간",
        #         wakeup_condition=["개운하다", "머리가 아프다"],
        #         wakeup_condition_etc="없엉",
        #         wakeup_first_thing="찬물 혹은 찬음료를 마신다",
        #         wakeup_first_thing_etc="없지용",
        #         meal="굶었엉",
        #         meal_during=["대화를 많이 하는 편이다", "먹는 것에 집중하는 편이다", "TV, 스마트폰 등을 보면서 먹는다"],
        #         meal_during_etc="안행",
        #         meal_with_water="안한다",
        #         meal_with_snack="안한다",
        #         meal_with_night_food="안한다",
        #         after_lunch=[
        #             "스마트폰을 본다",
        #             "밖에 나가 걷거나 산책을 한다",
        #             "담배를 핀다",
        #             "커피 등 후식을 즐긴다",
        #             "수다를 즐긴다",
        #             "잠이 쏟아진다",
        #         ],
        #         after_lunch_etc="없엉",
        #         saying=["말의 속도가 빠르다", "듣는 것보다 말하는 것에 더 익숙하다", "상대방의 말을 잘 듣는 편이다"],
        #         saying_etc="없엉",
        #     )
        return types.SubmitHabitCheckListResponse(ok=True)


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
            checkListQuestions = models.CheckListQuestion.objects.all()
            return types.SubmitCheckListResponse(checkListQuestions=checkListQuestions)

        else:
            all_answers = models.CheckListAnswer.objects.all()
            all_answers.update(later_answer=False)
            true_answers = models.CheckListAnswer.objects.filter(
                question__uuid__in=true_answer_question_uuids, user=user,
            )
            true_answers.update(later_answer=True)
            user.has_later_check_list_submitted = True
            user.save()
            checkListQuestions = models.CheckListQuestion.objects.all()
            return types.SubmitCheckListResponse(checkListQuestions=checkListQuestions)
