from . import types, models
from graphql_jwt.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required
def resolve_get_check_list_questions(self, info, **kwargs):
    user = info.context.user
    checkListQuestions = models.CheckListQuestion.objects.all().order_by("created_at")
    try:
        checkListAnswers = user.checkListAnswers.all().order_by("question__created_at")
        return types.GetCheckListQuestionsResponse(checkListAnswers=checkListAnswers, checkListQuestions=checkListQuestions)
    except ObjectDoesNotExist:
        return types.GetCheckListQuestionsResponse(checkListAnswers=None, checkListQuestions=checkListQuestions)


@login_required
def resolve_get_habit_check_list_list(self, info):
    user = info.context.user
    habitCheckLists = models.HabitCheckList.objects.filter(user=user)
    return types.GetHabitCheckListListResponse(habitCheckLists=habitCheckLists)


@login_required
def resolve_get_habit_check_list_detail(self, info, **kwargs):
    habit_check_list_uuid = kwargs.get("habit_check_list_uuid")
    habitCheckList = models.HabitCheckList.objects.get(
        uuid=habit_check_list_uuid)
    return types.GetHabitCheckListDetailResponse(habitCheckList=habitCheckList)
