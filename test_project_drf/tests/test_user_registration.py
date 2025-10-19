from http import HTTPStatus
import pytest
from django.contrib.auth import get_user_model

from .constants import USER_DATA

User = get_user_model()


@pytest.mark.django_db
class TestUserRegistration:
    URL_SIGNUP = '/api/users/'
    URL_TOKEN = '/api/token/login/'

    def test_nodata_signup(self, client):
        """Эндпоинт регистрации существует."""
        response = client.post(self.URL_SIGNUP)
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.URL_SIGNUP}` не найден.'
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            f'Ожидался статус 400, получен {response.status_code}. '
            f'Ответ: {response.content}'
        )

    def test_valid_user_registration(self, client, user_data):
        """Тест успешной регистрации пользователя."""
        response = client.post(self.URL_SIGNUP, data=user_data)
        assert response.status_code == HTTPStatus.CREATED, (
            f'Ожидался статус 201, получен {response.status_code}. '
            f'Ответ: {response.content}'
        )
        assert User.objects.filter(username=USER_DATA['username']).exists(), (
            'Пользователь не создан в базе данных'
        )

    def test_duplicate_username(self, client, existing_user):
        """Тест регистрации с существующим username."""
        response = client.post(self.URL_SIGNUP, data=existing_user)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Ожидалась ошибка при создании '
            'пользователя с существующим username'
        )

    def test_token_endpoint_exists(self, client):
        """Эндпоинт получения токена существует."""
        response = client.post(self.URL_TOKEN)
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            'Эндпоинт получения токена не найден.'
        )

    def test_get_token(self, client, existing_user, user_credentials):
        """Тест успешного получения токена."""
        response = client.post(self.URL_TOKEN, data=user_credentials)
        assert response.status_code == HTTPStatus.OK, (
            f'Ожидался статус 200, получен {response.status_code}.'
        )
        data = response.json()
        assert 'auth_token' in data, 'В ответе отсутствует auth_token'
        assert data['auth_token'], 'Токен не должен быть пустым'

    def test_get_token_invalid_credentials(self, client):
        """Получение токена с неверными учетными данными."""
        invalid_credentials = {
            'username': 'Вася',
            'password': '1234'
        }
        response = client.post(self.URL_TOKEN, data=invalid_credentials)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Ожидался статус 400 для неверных учетных данных.'
        )
