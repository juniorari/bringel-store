

def main():
    fake: Faker = Faker('pt_BR')
    fake.add_provider(ProviderEcommerce)

    for _ in range(5):
        obj = Supplier.objects.create(
            name=fake.company() + " " + fake.company_suffix(),
            email=fake.email(),
            address=fake.address()
        )
        print(f"Fornecedor: {obj.name}")

    for _ in range(50):
        obj = Product.objects.create(
            name=fake.ecommerce_name(),
            sku=fake.pyint(1000000000, 9999999999),
            categorie=fake.ecommerce_category(),
            price=fake.pyfloat(positive=True, right_digits=2, left_digits=4),
            supplier_id=random.randint(1, 5)
        )
        print(f"Produto: {obj.name}")

    for _ in range(10):
        obj = Client.objects.create(
            name=fake.name(),
            username=fake.user_name(),
            email=fake.email(),
            cpf=fake.cpf(),
            password=make_password(fake.password())
        )
        print(f"Cliente: {obj.name}")

    for _ in range(100):
        obj = RatingProduct.objects.create(
            client_id=random.randint(1, 10),
            product_id=random.randint(1, 50),
            rating=random.randint(1, 5),
        )
        print(f"Avaliação: {obj.id} - [{obj.product_id} - {obj.client_id}]")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bringel.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker
    from api.models import Product, Supplier, Client, RatingProduct
    from django.contrib.auth.hashers import make_password
    from utils.faker_ecommerce import ProviderEcommerce

    main()
