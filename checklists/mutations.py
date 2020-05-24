import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class SubmitHabitCheckList(graphene.Mutation):
    class Arguments:
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
        saying_repeat = graphene.String()
        walking = graphene.List(graphene.String)
        walking_etc = graphene.String()
        posture = graphene.List(graphene.String)
        posture_etc = graphene.String()
        posture_detail = graphene.List(graphene.String)
        posture_detail_etc = graphene.String()
        body_heat = graphene.List(graphene.String)
        body_heat_etc = graphene.String()
        exercise = graphene.String()
        sleeping = graphene.List(graphene.String)
        sleeping_etc = graphene.String()
        before_sleeping = graphene.List(graphene.String)
        before_sleeping_etc = graphene.String()
        good_thing = graphene.String()
        bad_thing = graphene.String()

    Output = types.SubmitHabitCheckListResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
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
        saying_repeat = kwargs.get("saying_repeat")
        walking = kwargs.get("walking")
        walking_etc = kwargs.get("walking_etc")
        posture = kwargs.get("posture")
        posture_etc = kwargs.get("posture_etc")
        posture_detail = kwargs.get("posture_detail")
        posture_detail_etc = kwargs.get("posture_detail_etc")
        body_heat = kwargs.get("body_heat")
        body_heat_etc = kwargs.get("body_heat_etc")
        exercise = kwargs.get("exercise")
        sleeping = kwargs.get("sleeping")
        sleeping_etc = kwargs.get("sleeping_etc")
        before_sleeping = kwargs.get("before_sleeping")
        before_sleeping_etc = kwargs.get("before_sleeping_etc")
        good_thing = kwargs.get("good_thing")
        bad_thing = kwargs.get("bad_thing")

        habitCheckList = models.HabitCheckList.objects.create(
            user=user,
            job=job,
            wakeup_time=wakeup_time,
            wakeup_long=wakeup_long,
            wakeup_condition=wakeup_condition,
            wakeup_condition_etc=wakeup_condition_etc,
            wakeup_first_thing=wakeup_first_thing,
            wakeup_first_thing_etc=wakeup_first_thing_etc,
            meal=meal,
            meal_during=meal_during,
            meal_during_etc=meal_during_etc,
            meal_with_water=meal_with_water,
            meal_with_snack=meal_with_snack,
            meal_with_night_food=meal_with_night_food,
            after_lunch=after_lunch,
            after_lunch_etc=after_lunch_etc,
            saying=saying,
            saying_etc=saying_etc,
            saying_repeat=saying_repeat,
            walking=walking,
            walking_etc=walking_etc,
            posture=posture,
            posture_etc=posture_etc,
            posture_detail=posture_detail,
            posture_detail_etc=posture_detail_etc,
            body_heat=body_heat,
            body_heat_etc=body_heat_etc,
            exercise=exercise,
            sleeping=sleeping,
            sleeping_etc=sleeping_etc,
            before_sleeping=before_sleeping,
            before_sleeping_etc=before_sleeping_etc,
            good_thing=good_thing,
            bad_thing=bad_thing,
        )
        user.has_habit_check_list_submitted = True
        user.save()
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
