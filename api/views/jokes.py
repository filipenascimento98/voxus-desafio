from rest_framework import viewsets
from rest_framework.response import Response
from api.domain.jokes import JokesDomain


class JokesView(viewsets.ViewSet):
    domain = JokesDomain()

    def get_random_joke(self, request):
        response = self.domain.get_random_joke()

        if isinstance(response, tuple):
            return Response({"message": response[1]}, status=response[0])

        return Response({"message": response}, status=200)
    
    def get_category_random_joke(self, request, category):
        response = self.domain.get_category_random_joke(str(category))

        if isinstance(response, tuple):
            return Response({"message": response[1]}, status=response[0])
        
        return Response({"message": response}, status=200)
    
    def get_filter_random_joke(self, request):
        response = self.domain.get_filter_random_joke(
            search=request.query_params.get('search', None),
            limit=request.query_params.get('limit', None)
        )

        if isinstance(response, tuple):
            return Response({"message": response[1]}, status=response[0])
        
        return Response({"message": response}, status=200)