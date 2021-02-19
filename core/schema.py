import graphene
from apps.users import schema as userSchema


class Query(userSchema.Query, graphene.ObjectType):
    pass


# class Mutation(userSchema.Mutation, graphene.ObjectType,):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=userSchema.Mutation)
