from django.shortcuts import render

# Create your views here.
def zone_geographique(request):
    return render(request, "zone_geographique/index.html")


def carte_villes(request):
    villes = [
        {'nom': 'Notre-Dame-de-Riez', 'info': ''},
        {'nom': 'Froidfond', 'info': 'environ 5 km au nord'},
        {'nom': 'Falleron', 'info': 'environ 8 km au nord-est'},
        {'nom': 'Saint-Paul-Mont-Penit', 'info': 'environ 8 km à l\'est'},
        {'nom': 'Grand\'Landes', 'info': 'environ 8 km au sud-est'},
        {'nom': 'Apremont', 'info': 'environ 8 km au sud'},
        {'nom': 'La Garnache', 'info': 'environ 9 km à l\'ouest'},
        {'nom': 'Commequiers', 'info': 'environ 9 km au sud-ouest'},
        {'nom': 'Challans', 'info': 'environ 9 km à l\'ouest'},
        {'nom': 'Maché', 'info': 'environ 10 km au sud-est'},
        {'nom': 'Saint-Étienne-du-Bois', 'info': 'environ 12 km à l\'est'},
        {'nom': 'Le Fenouiller', 'info': 'environ 14 km au sud-ouest'},
        {'nom': 'Soullans', 'info': 'environ 14 km à l\'ouest'},
        {'nom': 'Saint-Gervais', 'info': 'environ 15 km au nord-ouest'},
        {'nom': 'Beauvoir-sur-Mer', 'info': 'environ 15 km au nord-ouest'},
        {'nom': 'Saint-Hilaire-de-Riez', 'info': 'environ 15 km au sud-ouest'},
        {'nom': 'Saint-Gilles-Croix-de-Vie', 'info': '≈ 16 km au sud-ouest'},
        {'nom': 'Coëx', 'info': ''},
        {'nom': 'Legé', 'info': ''},
        {'nom': 'Saint-Étienne-du-Bois', 'info': ''},
        {'nom': 'Saint-Étienne-de-Mer-Morte', 'info': ''}
    ]

    return render(request, 'ma_carte.html', {'villes': villes})