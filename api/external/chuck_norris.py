import requests


class ApiChuckNorris:
    def __init__(self):
        self.url_base = 'http://api.chucknorris.io'
    
    def __build_url(self, url):
        return self.url_base + url
    
    def get_random_joke(self):
        '''
            Método responsável por coletar uma piada aleatória.
            Return:
                - value (string): Piada aleatória.
        '''
        url = self.__build_url('/jokes/random')
        response = requests.get(url=url).json()

        if response.get('status'):
            if response['status'] == 404:
                return (404, response['message'])

        return response['value']
    
    def get_category_random_joke(self, category):
        '''
            Método responsável por coletar uma piada aleatória para a categoria escolhida.
            Args:
                - category(string): Categoria da piada.
            Return:
                - value(string): Piada aleatória da categoria especificada.
        '''
        url = self.__build_url(f'/jokes/random?category={category}')
        response = requests.get(url=url).json()

        if response.get('status'):
            if response['status'] == 404:
                return (404, response['message'])

        return response['value']
    
    def get_filter_random_joke(self, query, limit):
        '''
            Método responsável por coletar uma piada aleatória para a palavra escolhida.
            Args:
                - query(string): Palavra a ser usada na pesquisa das piadas.
                - limit(int): Quantidade máxima de piadas.
            Return:
                - value(string): Piada(s) aleatória(s) da com base na palavra especificada.
        '''
        url = self.__build_url(f'/jokes/search?query={query}')
        response = requests.get(url=url).json()

        if response.get('status'):
            if response['status'] == 404 or response['status'] == 400:
                return (response['status'], response['message'])
        
        if response['total'] == 0:
            return (404, "No jokes found.")

        return response['result'][:limit]