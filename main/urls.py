from django.urls import path
from . import views  # Importing views

urlpatterns = [
    path('page2/', views.page2, name='page2'),  # Path for the page2 view
    path('save-favorite/', views.save_favorite_pokemon, name='save_favorite'),  # Path for saving favorite Pokémon
    path('show-all-pokemon/', views.show_all_pokemon, name='show_all_pokemon'),  # Path for displaying all Pokémon
]