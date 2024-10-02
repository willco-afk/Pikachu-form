from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FavoritePokemon

# View for the page2
def page2(request):
    return render(request, 'page2.html')  # Render the page2.html template

# View for saving favorite Pokémon
def save_favorite_pokemon(request):
    if request.method == 'POST':
        favorite_name = request.POST.get('favorite_pokemon')
        FavoritePokemon.objects.create(name=favorite_name)  # Save to the database
        return JsonResponse({'message': 'Favorite Pokémon saved successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# View for showing all favorite Pokémon
def show_all_pokemon(request):
    favorites = FavoritePokemon.objects.all()  # Get all favorite Pokémon from the database
    favorite_names = [pokemon.name for pokemon in favorites]  # Extract names into a list
    return JsonResponse({'pokemons': favorite_names})  # Return as JSON response

# New home view (optional)
def home(request):
    return redirect('page2')  # Redirect to the page2 view (optional)