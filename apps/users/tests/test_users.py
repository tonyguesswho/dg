# import json

from graphene_django.utils.testing import GraphQLTestCase


class UserTestCase(GraphQLTestCase):
    def test_get_users(self):
        response = self.query(
            '''
            query {
                users {
                email
                }
            }
            '''
        )
        self.assertResponseNoErrors(response)
