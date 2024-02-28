"""Provider for Faker which adds fake microservice names."""

import random

import faker.providers

CATEGORIES = [
    "Livros",
    "Filmes",
    "Música",
    "Jogos",
    "Eletrônicos",
    "Computadores",
    "Lar",
    "Jardim",
    "Ferramentas",
    "Mercado",
    "Saúde",
    "Beleza",
    "Brinquedos",
    "Crianças",
    "Bebê",
    "Roupas",
    "Sapato",
    "Jóias",
    "Esportes",
    "Ao ar livre",
    "Automotivo",
    "Industrial"
]

PRODUCT_DATA = {
    'material': [
        "Aço",
        "De madeira",
        "Concreto",
        "Plástico",
        "Algodão",
        "Granito",
        "Borracha",
        "Metal",
        "Macio",
        "Fresco",
        "Congeladas"
    ],
    'produto': [
        "Cadeira",
        "Carro",
        "Computador",
        "Teclado",
        "Rato",
        "Bicicleta",
        "Bola",
        "Luvas",
        "Calça",
        "Camisa",
        "Mesa",
        "Sapato",
        "Chapéu",
        "Toalhas",
        "Sabão",
        "Atum",
        "Frango",
        "Peixe",
        "Queijo",
        "Bacon",
        "Pizza",
        "Salada",
        "Salsichas",
        "Salgadinhos"
    ],
    'adjetivo': [
        "Pequeno",
        "Ergonômico",
        "Rústico",
        "Inteligente",
        "Maravilhoso",
        "Incrível",
        "Fantástico",
        "Prático",
        "Lustroso",
        "Incrível",
        "Genérico",
        "Feito à mão",
        "Feito à mão",
        "Licenciado",
        "Refinado",
        "Sem marca",
        "Saboroso",
        "Novo",
        "Usado suavemente",
        "Usado",
        "Para reparar"
    ]
}


class ProviderEcommerce(faker.providers.BaseProvider):

    def ecommerce_name(self):
        product = self.random_element(PRODUCT_DATA['produto'])
        adjective = self.random_element(PRODUCT_DATA['adjetivo'])
        material = self.random_element(PRODUCT_DATA['material'])

        choices = [
            product,
            " ".join([adjective, product]),
            " ".join([material, product]),
            " ".join([adjective, material, product]),
        ]

        names = random.choices(choices, k=1)
        return names[0]

    def ecommerce_category(self):
        """Fake categories names."""
        return self.random_element(CATEGORIES)

    def categories():
        lista = [];
        for i in CATEGORIES:
            lista.append((i, i))
        return tuple(lista)