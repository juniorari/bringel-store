from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class ClientURLsTest(TestCase):

    def test_client_home_url_is_correct(self):
        url = reverse('client:clients')
        self.assertEqual(url, '/client/')

    def test_client_read_url_is_correct(self):
        url = reverse('client:read_client', kwargs={'pk': 1})
        self.assertEqual(url, '/client/list/1')

    def test_client_read_url_is_incorrect(self):
        url = reverse('client:read_client', kwargs={'pk': 1})
        self.assertNotEqual(url, '/client/1000000')


class ClientHTTPResponseTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'testeuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)

    def get_jwt_access_token(self):
        # Chama a URL para obter o token de autenticação
        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)

        # Captura o token do response
        token = response.data.get('access')
        return token

    def test_client_read_http_200(self):
        Client.objects.create(
            name='Teste Nome',
            username='testenome',
            email='email@email.com',
            cpf='586.637.320-31',
            password='123456'
        )

        url = reverse('client:read_client', kwargs={'pk': 2})
        response = self.client.get(
            url, HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_read_http_404(self):
        url = reverse('client:read_client', kwargs={'pk': 1})
        response = self.client.get(
            url, HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_client_error_validation_required_field_cpf_400(self):
        post_data = {
            'name': 'Teste Cliente',
            'username': 'testenome',
            'password': '123456',
            'email': 'email@teste.net',
        }
        url = reverse('client:create_client')
        response = self.client.post(
            url, post_data,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
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
        response = self.client.post(
            url, post_data,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
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
        response = self.client.post(
            url,
            post_data,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_list_client_must_send_jwt_token(self):
        Client.objects.create(
            name="usuario teste",
            username="adminteste",
            password="654321",
            cpf="503.467.930-25",
            email="email@email.scsom",
        )
        api_url = reverse('client:clients')
        response = self.client.get(
            api_url,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_all_client(self):
        url = reverse('client:clients')
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(response.data.get('count'), 0)

    def test_update_client_success_update_200(self):
        post_data = {
            'name': 'Teste Cliente',
            'username': 'testenome',
            'password': '123456',
            'email': 'email@teste.net',
            'cpf': '405.664.140-40'
        }
        url = reverse('client:create_client')
        print(url)
        response = self.client.post(
            url, post_data,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        id = response.data.get('id')

        url = reverse('client:clients')
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        print(response.data)

        post_data = {
            'name': 'Teste Cliente 2',
            'username': 'teste2',
            'cpf': '405.664.140-40'
        }
        url = reverse('client:update_client', kwargs={'pk': id})
        response = self.client.put(
            url,
            post_data,
            HTTP_AUTHORIZATION=f'Bearer {self.get_jwt_access_token()}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
