from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class ClientURLsTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_client_home_url_is_correct(self):
        url = reverse('client:clients')
        self.assertEqual(url, '/client/')

    def test_client_read_url_is_correct(self):
        url = reverse('client:readclient', kwargs={'pk': 1})
        self.assertEqual(url, '/client/1')

    def test_client_read_url_is_incorrect(self):
        url = reverse('client:readclient', kwargs={'pk': 1})
        self.assertNotEqual(url, '/client/1000')

    def test_client_read_url_not_found(self):
        url = reverse('client:readclient', kwargs={'pk': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
