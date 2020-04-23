from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_all_classes(self, info):
    clasees = models.ClassOrder.objects.all()
    return types.GetAllClassesReponse(clasees=clasees)
 