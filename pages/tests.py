from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

HTTP_OK = 200


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        self.assertEqual(self.client.get('/').status_code, HTTP_OK)

    def test_view_url_by_name(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, HTTP_OK)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    username = 'new_user'
    email = 'new_user@mail.com'

    def test_signup_page_status_code(self):
        self.assertEqual(self.client.get('/users/signup/').status_code, HTTP_OK)

    def test_view_url_by_name(self):
        self.assertEqual(self.client.get(reverse('signup')).status_code, HTTP_OK)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)
