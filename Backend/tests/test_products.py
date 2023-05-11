from django.test import TestCase


class ProductsViewsTestCase(TestCase):
    def test_products_list_api(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8800/api/v1/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_create_api(self):
        """The index page loads properly"""
        payload = {
            "name": "Product 1",
            "description": "this is a test",
            "price": "123.00",
            "tax": "12.00",
            "stock": 9,
        }
        response = self.client.post('http://localhost:8800/api/v1/products/',
                                    payload)
        self.assertEqual(response.status_code, 200)

    def test_products_detail_api(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8800/api/v1/products/1/')
        self.assertEqual(response.status_code, 200)

    def test_products_update_api(self):
        """The index page loads properly"""
        payload = {
            "name": "Product 2",
            "description": "this is a update test",
            "price": "123.00",
            "tax": "12.00",
            "stock": 9,
        }
        response = self.client.put('http://localhost:8800/api/v1/products/1/',
                                   payload)
        self.assertEqual(response.status_code, 200)

    def test_products_remove_api(self):
        """The index page loads properly"""
        response = self.client.delete(
            'http://localhost:8800/api/v1/products/1/')
        self.assertEqual(response.status_code, 200)


