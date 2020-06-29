from . import types, models
from graphql_jwt.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required
def resolve_get_check_list_questions(self, info, **kwargs):
    user = info.context.user
    checkListQuestions = models.CheckListQuestion.objects.all()
    try:
        checkListAnswers = user.checkListAnswers.all()
        return types.GetCheckListQuestionsResponse(checkListAnswers=checkListAnswers, checkListQuestions=None)
    except ObjectDoesNotExist:
        return types.GetCheckListQuestionsResponse(checkListAnswers=None, checkListQuestions=checkListQuestions)


@ login_required
def resolve_get_habit_check_list(self, info):
    user = info.context.user
    try:
        habitCheckList = user.habitchecklist
        return types.GetHabitCheckListResponse(habitCheckList=habitCheckList)
    except ObjectDoesNotExist:
        return types.GetHabitCheckListResponse(habitCheckList=None)
