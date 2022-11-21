# Bienvenu sur notre application POKEDEX !

## Description
On utilise l'API de [Pokeapi](https://pokeapi.co/).

## Commandes

### Initialiser l'environnement

- pip install virtualenv
- py -m venv pokedexEnv
- En Powershell : cd ../pokedexEnv/Scripts/activate 
- (puis deactivate pour ne plus être dans l'environnement)

### On se replace à la racine de l'environnement
- cd ../..
- pip install Django
- pip install Requests

### Migrer dans la BDD
- py manage.py makemigrations (dans le cas ou l'on a modifié le modèle)
- py manage.py migrate

### Lancer le projet en local
- py manage.py runserver

---
<p align="center">
    <strong>Mathias LEROY, Alexis BERTIN, Julien LEDOUX</strong>
</p>
<p align="center">
    <strong> EPSI NANTES - 2022-2023</strong>
</p>