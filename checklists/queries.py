from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_check_list_answers(self, info, **kwargs):
    user = info.context.user
    checkListAnswers = models.CheckListQuestion.objects.all()

    return types.GetCheckListAnswersResponse(checkListAnswers=checkListAnswers)
