from django.urls import path
from api.views.jokes import JokesView


urlpatterns = [
    path('jokes/random', 
        JokesView.as_view({'get': 'get_random_joke'}), 
        name='random_joke'
    ),
    path('jokes/category/<category>', 
        JokesView.as_view({'get': 'get_category_random_joke'}), 
        name='category_random_joke'
    ),
    path('jokes/filter',
        JokesView.as_view({'get': 'get_filter_random_joke'}),
        name='filter_random_joke',
    )
]
