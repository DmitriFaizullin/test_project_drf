from http import HTTPStatus
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestProductAPI:
    """Тесты для API продуктов."""
    URL_PRODUCTS = '/api/products/'

    def test_products_list_endpoint(self, client):
        """Эндпоинт списка продуктов существует."""
        response = client.get(self.URL_PRODUCTS)
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт продуктов {self.URL_PRODUCTS} не найден!'
        )

    def test_products_list_returns_200(self, client):
        """Эндпоинт списка продуктов возвращает статус 200."""
        response = client.get(self.URL_PRODUCTS)
        assert response.status_code == HTTPStatus.OK, (
            f'Ожидался статус 200, получен {response.status_code}'
        )

    def test_pagination_structure(self, client, create_test_product):
        """Пагинация списка продуктов настроена."""
        response = client.get(self.URL_PRODUCTS)
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) == 4, f'Ожидалось 4 поля, получено {len(data)}'
        expected_fields = ['count', 'next', 'previous', 'results']
        for field in expected_fields:
            assert field in data, f'В ответе отсутствует поле {field}'

    def test_products_list_count(self, client, create_test_product):
        """Продукт создается в базе."""
        response = client.get(self.URL_PRODUCTS)
        data = response.json()
        assert len(data['results']) == 1, (
            f'Ожидался 1 продукт, получено {len(data)}')

    def test_products_detail_nonexistent(self, client):
        """Запрос несуществующего продукта."""
        url = reverse('products-detail', kwargs={'pk': 100500})
        response = client.get(url)
        assert response.status_code == HTTPStatus.NOT_FOUND, (
            f'Ожидался статус 404 для несуществующего'
            f'продукта, получен {response.status_code}'
        )

    def test_products_list_structure(
            self, client, create_test_product):
        """Тест структуры ответа списка продуктов."""
        response = client.get(self.URL_PRODUCTS)
        products = response.json()['results']
        assert isinstance(products, list), 'Список продуктов типа list'
        product = products[0]
        expected_fields = ['name', 'slug', 'category',
                           'subcategory', 'price', 'images']
        for field in expected_fields:
            assert field in product, f'В ответе отсутствует поле {field}'
        assert isinstance(product['images'],
                          list), 'images должен быть списком'
