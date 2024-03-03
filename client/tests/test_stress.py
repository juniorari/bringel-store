from locust import HttpUser, between, task
from django.urls import reverse


class WebsiteUser(HttpUser):
    # espera entre 5 e 15 segundos entre cada requisição
    wait_time = between(min_wait=1, max_wait=3)

    @task
    def view_client_page(self):
        self.client.get(reverse('client:clients'))

    @task
    def view_product_page(self):
        self.client.get(reverse('product:products'))

    @task
    def view_home_page(self):
        self.client.get(reverse('welcome'))
