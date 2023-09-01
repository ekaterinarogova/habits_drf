from rest_framework.test import APITestCase
from rest_framework import status


class UserTestCase(APITestCase):

    def test_register_user(self):
        """Тестирование регистрации нового пользователя"""
        data = {
            'username': 'test',
            'password': '12345',
            'telegram_id': 438355578
        }
        response = self.client.post('/users/register/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


