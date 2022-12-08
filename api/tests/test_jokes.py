from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class JokesTest(TestCase):
    def setUp(self):
        self.api_client = APIClient()
    
    def test_get_random_joke(self):
        """
            GET - Obtém uma piada aleatória
        """
        response = self.api_client.get(reverse('random_joke'), format='json')

        # Verifico:
        # - Se o status é 200
        # - Se a resposta é uma string
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['message'], str)
    
    def test_get_category_random_joke(self):
        """
            GET - Obtém uma piada aleatória de acordo com a categoria 'animal'
        """
        response = self.api_client.get(reverse('category_random_joke', args=['animal']), format='json')

        # Verifico:
        # - Se o status é 200
        # - Se a resposta é uma string
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['message'], str)
    
    def test_get_category_random_joke_return_404(self):
        """
            GET - Obtém 404 ao tentar buscar uma piada de uma categoria que não existe.
        """
        response = self.api_client.get(reverse('category_random_joke', args=['filipe']), format='json')

        # Verifico:
        # - Se o status é 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_filter_random_joke(self):
        """
            GET - Obtém uma piada aleatória de acordo com a palavra usada no filtro e quantidade de acordo com o limite.
        """
        search = 'house'
        amount_of_jokes = 10
        response = self.api_client.get(reverse('filter_random_joke'), {'search': search, 'limit': amount_of_jokes}, format='json')

        # Verifico:
        # - Se o status é 200
        # - Se a quantidade de piadas é menor ou igual ao limite
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(len(response.data['message']), amount_of_jokes)
    
    def test_get_filter_random_joke_return_404(self):
        """
            GET - Obtém 404 ao tentar buscar uma piada com uma palavra de busca que não existe.
        """
        search = 'filipe'
        amount_of_jokes = 10
        response = self.api_client.get(reverse('filter_random_joke'), {'search': search, 'limit': amount_of_jokes}, format='json')

        # Verifico:
        # - Se o status é 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_filter_random_joke_return_400(self):
        """
            GET - Obtém 400 ao tentar buscar uma piada sem uma palavra de busca ou sem limite.
        """
        search = 'filipe'
        amount_of_jokes = 10
        # Faz a requisição sem o 'limit'
        response_without_limit = self.api_client.get(reverse('filter_random_joke'), {'search': search}, format='json')

        # Verifico:
        # - Se o status é 400
        self.assertEqual(response_without_limit.status_code, status.HTTP_400_BAD_REQUEST)
    
        # Faz a requisição sem o 'search'
        response_without_search = self.api_client.get(reverse('filter_random_joke'), {'limit': amount_of_jokes}, format='json')

        # Verifico:
        # - Se o status é 400
        self.assertEqual(response_without_search.status_code, status.HTTP_400_BAD_REQUEST)
