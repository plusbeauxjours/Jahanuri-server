import graphene
from graphql_jwt.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from graphene_file_upload.scalars import Upload
from . import types, models


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    Output = types.CreateUserResponse

    def mutate(self, info, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        user = get_user_model()(
            username=username, first_name=first_name, last_name=last_name,
        )
        user.set_password(password)
        user.save()

        return types.CreateUserResponse(ok=True, user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        user_img = Upload()
        address = graphene.String()
        job = graphene.String()
        phone_number = graphene.String()
        email = graphene.String()

    Output = types.UpdateUserResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        first_name = kwargs.get("first_name", "")
        last_name = kwargs.get("last_name", "")
        password = kwargs.get("password", "")
        user_img = kwargs.get("user_img", None)
        address = kwargs.get("address", "")
        job = kwargs.get("job", "")
        phone_number = kwargs.get("phone_number", "")
        email = kwargs.get("email", "")

        if first_name != "":
            user.first_name = first_name
        if last_name != "":
            user.last_name = last_name
        if password != "":
            user.set_password(password)
        if user_img is not None:
            user.user_img = user_img
        user.address = address
        user.job = job
        user.phone_number = phone_number
        user.email = email

        user.save()

        return types.UpdateUserResponse(user=user)


class RemoveUser(graphene.Mutation):
    class Arguments:
        uuid = graphene.String(required=True)

    Output = types.RemoveUserResponse

    @login_required
    def mutate(self, info, **kwargs):
        uuid = kwargs.get("uuid", "")
        user = models.User.objects.get(uuid=uuid)
        user.delete()

        return types.RemoveUserResponse(ok=True)
