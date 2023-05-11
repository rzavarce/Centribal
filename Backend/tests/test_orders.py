from django.test import TestCase


class OrdersViewsTestCase(TestCase):
    def test_orders_list_api(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8800/api/v1/orders/')
        self.assertEqual(response.status_code, 200)

    def test_orders_create_api(self):
        """The index page loads properly"""
        payload = {
            "order_detail": [
                {"id": 1, "quantity": 1},
                {"id": 2, "quantity": 2},
                {"id": 3, "quantity": 3}
            ]
        }
        response = self.client.post('http://localhost:8800/api/v1/orders/',
                                    payload)
        self.assertEqual(response.status_code, 200)

    def test_orders_detail_api(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8800/api/v1/orders/1/')
        self.assertEqual(response.status_code, 200)

    def test_orders_update_api(self):
        """The index page loads properly"""
        payload = {
            "order_detail": [
                {"id": 4, "quantity": 3},
                {"id": 5, "quantity": 2},
                {"id": 6, "quantity": 1}
            ]
        }
        response = self.client.put('http://localhost:8800/api/v1/orders/1/',
                                   payload)
        self.assertEqual(response.status_code, 200)

    def test_orders_remove_api(self):
        """The index page loads properly"""
        response = self.client.delete(
            'http://localhost:8800/api/v1/orders/1/')
        self.assertEqual(response.status_code, 200)


