import pytest
import datetime
from django.urls import reverse
from django.test import TestCase
from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError

from .models import Products

"""
class TestProductsManager:

    def test_list_products(self, mocker):
        expected_results = [
            Products(
                reference='P-123456-1',
                name='Products Test',
                description="This is a test",
                price=123,
                tax=21.0,
                stock=20,
                status=True,
                created=datetime.datetime.now(),
                modified=datetime.datetime.now()
            )
        ]

        qs = MockSet(expected_results[0])
        mocker.patch.object(Products.objects, 'get_queryset', return_value=qs)
"""


class ViewsTestCase(TestCase):
    def test_products_list_api(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8800/api/v1/products/')
        self.assertEqual(response.status_code, 200)



