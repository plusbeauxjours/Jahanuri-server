from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_me(self, info):
    user = info.context.user
    print("nnani")
    return types.MeReponse(user=user)