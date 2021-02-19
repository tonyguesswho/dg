import graphene
import graphql_jwt
from apps.users import schema as userSchema


class Query(userSchema.Query, graphene.ObjectType):
    pass


class Mutation(userSchema.Mutation, graphene.ObjectType,):
    login = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
