from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Client


class ClientURLsTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_client_home_url_is_correct(self):
        url = reverse('client:clients')
        self.assertEqual(url, '/client/')

    def test_client_read_url_is_correct(self):
        url = reverse('client:read_client', kwargs={'pk': 1})
        self.assertEqual(url, '/client/list/1')

    def test_client_read_url_is_incorrect(self):
        url = reverse('client:read_client', kwargs={'pk': 1})
        self.assertNotEqual(url, '/client/1000000')


class CLientHTTPResponseTest(TestCase):
    def test_client_read_http_200(self):
        Client.objects.create(
            name='Teste Nome',
            username='testenome',
            email='email@email.com',
            cpf='123.456.789-00',
            password='123456'
        )
        url = reverse('client:read_client', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_read_http_404(self):
        url = reverse('client:read_client', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_client_error_validation_required_field_cpf_400(self):
        post_data = {
            'name': 'Teste Cliente',
            'username': 'testenome',
            'password': '123456',
            'email': 'email@teste.net',
        }
        url = reverse('client:create_client')
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode(),
                         '{"cpf":["Este campo é obrigatório."]}')

    def test_create_client_error_validate_cpf(self):
        post_data = {
            'name': 'Teste Cliente',
            'username': 'testenome',
            'password': '123456',
            'email': 'email@teste.net',
            'cpf': '123.456.789-00'
        }
        url = reverse('client:create_client')
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode(),
                         '{"cpf":["O CPF 123.456.789-00 é inválido"]}')

    def test_create_client_success_create_201(self):
        post_data = {
            'name': 'Teste Cliente',
            'username': 'testenome',
            'password': '123456',
            'email': 'email@teste.net',
            'cpf': '621.609.153-00'
        }
        url = reverse('client:create_client')
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_update_client_success_update_200(self):
    #     post_data = {
    #         'name': 'Teste Cliente',
    #         'username': 'testenome',
    #         'password': '123456',
    #         'email': 'email@teste.net',
    #         'cpf': '621.609.153-00'
    #     }
    #     url = reverse('client:create_client')
    #     print(url)
    #     response = self.client.post(url, post_data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     post_data = {
    #         'name': 'Teste Cliente 2',
    #         'username': 'teste2'
    #     }
    #     url = '/client/update/1'
    #     response = self.client.put(url, post_data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
