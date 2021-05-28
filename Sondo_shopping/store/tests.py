import unittest

from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView
from django.test import TestCase, SimpleTestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from customers.forms import UserRegisterForm
from customers.views import register
from .views import Cart
from .views.home import ProductDetailView
from .views.serializerView import CustomerSerializer
from customers.models import Customer

from rest_framework.test import RequestsClient


class ApiTest(APITestCase):
    client = RequestsClient()
    response = client.get('http://localhost:8080/api/customers/')
    assert response.status_code == 200


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "Test1", "email": "test1@gmail.com", "password1": "Test1@Strong", "password2": "Test1@Strong"
        }
        response = self.client.post("/api/rst-auth/registration/", data)
        self.assertNotAlmostEqual(response.status_code, status.HTTP_201_CREATED)


# class CustomerViewSetTestCase(APITestCase):
#     list_url = reverse("customers-list")
#
#     def setUp(self):
#         self.user = User.objects.create_user(username="Zama",email="Zama@gmail.com",password="Zama@#$21")
#
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()
#
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
#
#     def test_customer_list_authenticated(self):
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

#     def test_customer_list_unauthenticated(self):
#         self.client.force_authenticate(user=None)
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

class TestUrls(SimpleTestCase):

    def test_product_detail(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_reset_done(self):
        url = reverse('password_reset_done')
        self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

    def test_reset_complete(self):
        url = reverse('password_reset_complete')
        self.assertEquals(resolve(url).func.view_class, PasswordResetCompleteView)


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.user1 = User(username='Zama', email='zama@gmail.com', password='Zama$2020')
        self.customer1 = Customer(customer=self.user1, phone='12345678')

    def test_name(self):
        self.assertEqual(self.customer1.customer.username, self.user1.username)
        self.assertEqual(self.customer1.customer.username, 'Zama')
        self.assertEqual(self.customer1.phone, '12345678')

    def test_email(self):
        self.assertNotEqual(self.customer1.customer.email.find('@'), -1)
        self.assertNotEqual(self.customer1.customer.email.find('.'), -1)


class TestForms(unittest.TestCase):

    def test_UserRegisterForm(self):
        form = UserRegisterForm(data={
            'username': 'Zamokuhle',
            'email': 'kuhle@gmail.com',
            'password1': 'Mokuhle@2021',
            'password2': 'Mokuhle@2021'
        })
        self.assertTrue(form.is_valid())

    def test_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())

    def test_unique_UserRegisterForm(self):
        form = UserRegisterForm(data={
            'username': 'djsbu',
            'email': 'zamokuhlemasondo6@gmail.com',
            'password1': 'Mokuhle@2021',
            'password2': 'Mokuhle@2021'
        })
        self.assertFalse(form.errors)
