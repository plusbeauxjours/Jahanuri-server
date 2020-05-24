from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_me(self, info):
    print("im here")
    user = info.context.user
    return types.MeReponse(user=user)


@login_required
def resolve_get_user_list(self, info):
    users = models.User.objects.all()
    return types.GetUserListResponse(users=users)


@login_required
def resolve_get_user(self, info, **kwargs):
    uuid = kwargs.get("uuid", None)

    if uuid:
        user = models.User.objects.get(uuid=uuid)
        return types.GetUserResponse(user=user)


@login_required
def resolve_get_class_users(self, info, **kwargs):
    class_order = kwargs.get("class_order", None)

    if class_order:
        users = models.User.objects.filter(class_order__order=class_order)
        return types.GetClasstUsersResponse(users=users)
