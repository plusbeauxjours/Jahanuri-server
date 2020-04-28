from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_check_list_questions(self, info, **kwargs):
    user = info.context.user
    checkListQuestions = models.CheckListQuestion.objects.all()

    return types.GetCheckListQuestionsResponse(checkListQuestions=checkListQuestions)
