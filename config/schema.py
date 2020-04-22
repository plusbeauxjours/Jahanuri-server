import graphene
import graphql_jwt

from users import schema as user_schema
from classes import schema as class_schema
from checklists import schema as checklist_schema


class Query(
    user_schema.Query, class_schema.Query, checklist_schema.Query, graphene.ObjectType,
):
    pass


class Mutation(
    user_schema.Mutation,
    class_schema.Mutation,
    checklist_schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
