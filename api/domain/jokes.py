from api.external.chuck_norris import ApiChuckNorris


class JokesDomain:
    def __init__(self):
        self.api_chuck = ApiChuckNorris()
    
    def get_random_joke(self):
        data_joke = self.api_chuck.get_joke('/jokes/random')

        if isinstance(data_joke, tuple):
            return (data_joke[0], data_joke[1])
        
        return data_joke
    
    def get_category_random_joke(self, category=''):
        data_joke = self.api_chuck.get_joke(f'/jokes/random?category={str(category)}')

        if isinstance(data_joke, tuple):
            return (data_joke[0], data_joke[1])
        
        return data_joke
    
    def get_filter_random_joke(self, search, limit):
        if not search or not limit:
            return (400, "search and limit are required.")

        data_joke = self.api_chuck.get_filter_random_joke(query=str(search), limit=int(limit))

        if isinstance(data_joke, tuple):
            return (data_joke[0], data_joke[1])
        
        jokes = []
        for joke in data_joke:
            jokes.append(joke['value'])
        
        return jokes