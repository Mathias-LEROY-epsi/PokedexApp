from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
from .models import TeamModel
from .forms import TeamForm


# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ', '%20')
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            url_pokeapi.add_header('User-Agent', "pikachu")
            source = urllib.request.urlopen(url_pokeapi).read()
            # url_pokeapi_limit = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon?limit=898')
            # source_limit = urllib.request.urlopen(url_pokeapi_limit).read()

            # Convertir un JSON en un dictionnaire
            list_of_data = json.loads(source)
            # list_of_data_limit = json.loads(source_limit)

            # Calcul pour afficher en mètre
            height_obtained = (float(list_of_data['height']) * 0.1)
            height_rounded = round(height_obtained, 2)

            # Calcul pour afficher en kilogramme
            weight_obtained = (float(list_of_data['weight']) * 0.1)
            weight_rounded = round(weight_obtained, 2)

            data = {
                # "all_pokemons": list_of_data_limit['results'],
                "number": str(list_of_data['id']),
                "name": str(list_of_data['name']).capitalize(),
                "height": str(height_rounded) + " m",
                "weight": str(weight_rounded) + " kg",
                "image": str(list_of_data['sprites']['front_default']),
                # "type": ,
                "type1": str(list_of_data['types'][0]['type']['name']).capitalize(),
                # "type1": str(list_of_data['types'][0]['type']['name']).capitalize(),
                # "type2": str(list_of_data['types'][1]['type']['name']).capitalize(),
                # "abilities": {
                #     "ability1": str(list_of_data['abilities'][0]['ability']['name']).capitalize(),
                #     "ability2": str(list_of_data['abilities'][1]['ability']['name']).capitalize(),
                #     "ability3": str(list_of_data['abilities'][2]['ability']['name']).capitalize(),
                # },
                "hp": str(list_of_data['stats'][0]['base_stat']),
                "attack": str(list_of_data['stats'][4]['base_stat']),
                "defense": str(list_of_data['stats'][3]['base_stat']),
                "special_attack": str(list_of_data['stats'][2]['base_stat']),
                "special_defense": str(list_of_data['stats'][1]['base_stat']),
                "speed": str(list_of_data['stats'][5]['base_stat']),
                # "forms": {
                #     "form1": str(list_of_data['forms'][0]['name']).capitalize(),
                #     "form2": str(list_of_data['forms'][1]['name']).capitalize(),
                #     "form3": str(list_of_data['forms'][2]['name']).capitalize(),
                # },
            }

            print(data)
        else:
            data = {}

        return render(request, "index.html", data)
    except HTTPError as e:
        if e.code == HTTPStatus.NOT_FOUND:
            return render(request, "index.html", {"error": "Pokemon not found"})
        else:
            return render(request, "index.html", {"error": "Error"})


def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})


def teams(request):
    context = {"dataset": TeamModel.objects.all()}
    return render(request, 'teams.html', context)


def detail_team(request, team_id):
    context = {"data": TeamModel.objects.get(id=team_id)}
    return render(request, 'detail_team.html', context)


def update_team(request, team_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(TeamModel, id=team_id)

    # pass the object as instance in form
    form = TeamForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + team_id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_team.html", context)
