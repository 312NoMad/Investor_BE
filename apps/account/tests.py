from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from .models import CustomUser as User


class AccountTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@localhost.com',
            password='testpassword',
            first_name='',
            last_name=''
        )

    def test_signup(self):
        data1 = {
            'email': 'newuser@localhost.com',
            'password': 'newpassword',
            'first_name': '',
            'last_name': ''
        }
        data2 = {
            'email': 'testuser@localhost.com',
            'password': 'testpassword',
            'first_name': '',
            'last_name': ''
        }
        url = reverse('sign_up')

        response1 = self.client.post(url, data1, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response1.data.get('message'), 'User registered successfully')

        response2 = self.client.post(url, data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.data.get('email')[0], 'user with this email already exists.')

    def test_signin(self):
        data = {
            'email': 'testuser@localhost.com',
            'password': 'testpassword',
            'first_name': '',
            'last_name': ''
        }
        url = reverse('sign_in')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data.get('refresh')

    def test_refresh(self):
        data = {
            'refresh': self.test_signin()
        }
        url = reverse('token_refresh')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signout(self):
        refresh_token = self.test_signin()
        data = {
            'refresh': refresh_token
        }
        url = reverse('sign_out')
        url2 = reverse('token_refresh')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.post(url2, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response2.data, {"detail": "Token is blacklisted", "code": "token_not_valid"})
