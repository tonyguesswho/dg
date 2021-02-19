
from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.shortcuts import create_refresh_token, get_token


User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password',)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, name, password, email):
        user = User.objects.create_user(
            name=name, email=email, password=password)

        token = get_token(user)
        refresh_token = create_refresh_token(user)

        return CreateUser(user=user, token=token, refresh_token=refresh_token)


class Mutation(graphene.ObjectType):
    register = CreateUser.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        return user
