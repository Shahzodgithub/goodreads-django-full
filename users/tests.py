from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class LoginTestCase(TestCase):
    def test_user_account_is_created(self):
        db_user = User.objects.create_user(username='shahzod', first_name='shahzod')
        db_user.set_password('somepass')
        db_user.save()

        self.client.post(reverse('users:login'), data={
            'username': 'shahzod',
            'password': 'somepass'
        })

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_wrong_username(self):
        self.client.post(reverse('users:login'), data={
            'username': 'shahzod1',
            'password': 'somepass'
        })
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_wrong_password(self):
        self.client.post(reverse('users:login'), data={
            'username': 'shahzod',

            'password': '<PASSWORD>'
        })
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))
        # self.assertEqual(response.status_code, 200)

    def test_profile_details(self):
        user = User.objects.create_user(username='shahzod', first_name='shahzod',last_name='meo', email='me@mo.ml')
        user.set_password('momo9932')
        user.save()

        self.client.login(username='shahzod', password='momo9931')
        response = self.client.get(reverse('users:profile'))
        # self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        user = User.objects.create_user(username='shahzod', first_name='shahzod', last_name='meo', email='me@mo.ml')
        user.set_password('momo9932')
        user.save()

        self.client.login(username='shahzod', password='momo9931')
        # response = self.client.post(reverse('users:profile-edit'), data={
        #     'username': 'shahzod',
        #     'first_name': 'shahzod',
        #     'last_name': 'meo',
        #     'email': 'me@mo.ml',
        # })
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'shahzod')
        self.assertEqual(user.last_name, 'meo')
        self.assertEqual(user.email, 'me@mo.ml')
        self.assertEqual(user.username, 'shahzod')