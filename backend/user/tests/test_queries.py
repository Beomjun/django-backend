#!/usr/bin/env python
import json

from parameterized import parameterized

from backend.common.testcase import CustomGraphQLTestCase
from backend.user.tests.factories import UserFactory


class TestUserQueries(CustomGraphQLTestCase):

    def setUp(self) -> None:
        self.user = UserFactory(email='new@test.com')

        self.user_query = """
            query User($email: String!) {
                user(email: $email) {
                    email
                    username
                    firstName
                    lastName
                    lastAccessed
                }
            }
        """

    def test_user_query(self):
        response = self.query(self.user_query, variables={'email': 'no_user@test.com'})
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertIn('data', content)

        result = content['data']['user']
        self.assertIsNone(result)

        response = self.query(self.user_query, variables={'email': self.user.email})
        content = json.loads(response.content)
        self.assertIn('data', content)

        result = content['data']['user']
        self.assertEqual(self.user.email, result['email'])

    @parameterized.expand([
        ('password',),
        ('isSuperuser',),
        ('isStaff',)
    ])
    def test_not_allowed_user_query(self, field: str):
        response = self.query(
            """
            query User($email: String!) {
                user(email: $email) {
                    {field}
                }
            }
            """.replace('{field}', field),
            op_name='user',
            variables={'email': self.user.email}
        )

        self.assertResponseHasErrors(response)
