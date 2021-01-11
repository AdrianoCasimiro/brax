from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

class LogInTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('login'))
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)

    def test_login_page(self):
        self.assertEqual(200, self.response.status_code)

    def test_login_in_response(self):
        self.assertTrue(self.response.content, 'Log In')

    def test_login_user(self):
        response = self.client.post(r('login'), self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class LogOutTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)

    def test_login_user(self):
        self.response = self.client.post(r('login'), self.credentials, follow=True)
        self.assertTrue(self.response.context['user'].is_authenticated)

    def test_logout_user(self):
        response = self.client.get(r('logout'))
        self.assertEqual(response.status_code, 302)



