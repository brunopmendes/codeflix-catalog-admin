from django.test import TestCase
from rest_framework.test import APITestCase

class TestView(APITestCase):
    def test_get_categories(self):
        url = "/api/categories/"
        response = self.client.get(url)

        expected_data = [
            {
                "id": "87be2268-dcff-4f17-b1a6-421537d4ec98",
                "name": "Filme",
                "description": "Categoria para filmes",
                "is_active": True
            },
            {
                "id": "82552420-2c29-477b-91c6-265453c78dff",
                "name": "Série",
                "description": "Categoria para séries",
                "is_active": True
            }
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
        