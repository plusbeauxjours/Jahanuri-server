from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_check_list_list(self, info, **kwargs):
    user_uuid = kwargs.get("user_uuid", "")
    name = kwargs.get("name", "")

    if user_uuid != "":
        checkLists = models.CheckListAnswer.objects.filter(
            check_list_cover__user__uuid=user_uuid
        )
        return types.GetCheckListListReponse(checkLists=checkLists)
    elif name != "":
        checkLists = models.CheckListAnswer.objects.filter(check_list_cover__name=name)
        return types.GetCheckListListReponse(checkLists=checkLists)
    else:
        return types.GetCheckListListReponse(checkLists=None)
