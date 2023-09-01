from rest_framework.test import APITestCase, APIClient, RequestsClient
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user(
            username='test',
            password='12345',
            telegram_id=438344678)

        Habit.objects.create(
            user=User.objects.get(username='test'),
            place='test1',
            time='2023-10-10T12:00+00.00',
            action='test1',
            reward='test',
            realization_time=100,
            periodicity=2,
        )

    def test_update_habit(self):
        """Тестирование редактирования привычки"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        data = {
            'action': 'changed_data'
        }
        print(Habit.objects.get(action='test1').id)

        response = self.client.patch('/update/8/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['action'], 'changed_data')

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            'place': 'test',
            'time': '2023-10-10T12:00',
            'action': 'test',
            'reward': 'test',
            'realization_time': 100,
            'periodicity': 2
        }
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.post('/create/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_list_habit(self):
        """Тестирование выведения списка привычки"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/list/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_list_public_habit(self):
        """Тестирование выведение списка только публичных привычек"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/public_list/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 0)

    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.delete('/delete/5/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)


class HabitPermissionsTestCase(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user(
                username='test',
                password='12345',
                telegram_id=438344678
            )
        User.objects.create_user(
                username='test1',
                password='12345',
                telegram_id=438344678
            )

        Habit.objects.create(
                user=User.objects.get(username='test'),
                place='test1',
                time='2023-10-10T12:00+00.00',
                action='test1',
                reward='test',
                realization_time=100,
                periodicity=2,
            )

    def test_is_owner_permission_negative(self):
        """Тестирование права доступа для создателя привычки от другого пользователя"""
        token = self.client.post('/users/token/', data={'username': 'test1', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.delete('/delete/1/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_is_owner_permission_positive(self):
        """Тестирование права доступа для хозяина привычки от его создателя"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.delete('/delete/2/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)












