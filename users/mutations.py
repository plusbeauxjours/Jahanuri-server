import random
import json
import graphene
from graphql_jwt.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from . import types, models
from django.core.files.base import ContentFile
from io import BytesIO
from urllib.request import urlopen
from graphql_jwt.shortcuts import get_token


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


class AppleConnect(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        apple_id = graphene.String(required=True)

    Output = types.AppleConnectResponse

    def mutate(self, info, **kwargs):

        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        email = kwargs.get("email")
        apple_id = kwargs.get("apple_id")

        try:
            user = models.User.objects.get(apple_id=apple_id)
            token = get_token(user)
            return types.AppleConnectResponse(ok=True, token=token)

        except models.User.DoesNotExist:
            with open(
                "users/adjectives.json", mode="rt", encoding="utf-8"
            ) as adjectives:
                with open("users/nouns.json", mode="rt", encoding="utf-8") as nouns:
                    adjectives = json.load(adjectives)
                    nouns = json.load(nouns)
                    if email:
                        local, at, domain = email.rpartition("@")
                        username = random.choice(adjectives) + local.capitalize()
                    else:
                        username = (
                            random.choice(adjectives)
                            + random.choice(nouns).capitalize()
                        )

                    user = models.User.objects.create_user(username)
                    if first_name:
                        user.first_name = first_name
                    if last_name:
                        user.last_name = last_name
                    user.apple_id = apple_id
                    user.email = email
                    user.has_apple_account = True
                    user.save()

                    token = get_token(user)
                    return types.AppleConnectResponse(ok=True, token=token)


class KakaoConnect(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        kakao_id = graphene.String(required=True)

    Output = types.KakaoConnectResponse

    def mutate(self, info, **kwargs):

        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        email = kwargs.get("email")
        kakao_id = kwargs.get("kakao_id")

        try:
            user = models.User.objects.get(kakao_id=kakao_id)
            token = get_token(user)
            return types.KakaoConnectResponse(ok=True, token=token)

        except models.User.DoesNotExist:
            with open("users/adjectives.json", mode="rt", encoding="utf-8") as file:
                adjectives = json.load(file)
                if email:
                    local, at, domain = email.rpartition("@")
                username = random.choice(adjectives) + local.capitalize()

                # avatar_url = "https://graph.facebook.com/%s/picture?type=large" % kakao_id
                # user_img = BytesIO(urlopen(avatar_url).read())
                # user_img.save("image.jpg", ContentFile(user_img.getvalue()), save=False)
                # user_img.save()

                # user.user_img = user_img
                user = models.User.objects.create_user(username)
                user.kakao_id = kakao_id
                user.first_name = first_name
                user.last_name = last_name
                user.has_kakao_account = True
                user.save()

                token = get_token(user)
                return types.KakaoConnectResponse(ok=True, token=token)
