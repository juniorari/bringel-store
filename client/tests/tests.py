from django.test import TestCase

# Create your tests here.

class SimplePytestTest(TestCase):


    def test_the_pytest_is_ok(self):
        assert 1 == 1, 'Um é igual a um'


    def test_the_pytest_is_ok2(self):
        assert 2 == 2, 'Dois é igual a um'


        