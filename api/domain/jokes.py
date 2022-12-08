from api.external.chuck_norris import ApiChuckNorris


class JokesDomain:
    def __init__(self):
        self.api_chuck = ApiChuckNorris()
    
    def get_random_joke(self):
        data_joke = self.api_chuck.get_random_joke()

        if isinstance(data_joke, tuple):
            return (data_joke[0], data_joke[1])
        
        return data_joke
    
    def get_category_random_joke(self, category=''):
        data_joke = self.api_chuck.get_category_random_joke(category=category)

        if isinstance(data_joke, tuple):
            return (data_joke[0], data_joke[1])
        
        return data_joke
    
    def get_filter_random_joke(self, query='', limit=0):
        data_joke = self.api_chuck.get_filter_random_joke(query=query, limit=limit)

        if isinstance(data_joke, tuple):
            return (data_joke[0], data_joke[1])
        
        jokes = []
        for joke in data_joke:
            jokes.append(joke['value'])
        
        return jokes