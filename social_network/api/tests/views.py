from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class UserTests(APITestCase):

    def test_user_signup(self):
        url = reverse('user-signup')
        data = {'email': 'syedajaz91@gmail.com', 'password': 'syed@123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        User = get_user_model()
        user = User.objects.create_user(email='syedajaz91@gmail.com', password='syed@123')
        url = reverse('user-login')
        data = {'email': 'syedajaz91@gmail.com', 'password': 'syed@123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
