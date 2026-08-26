# Mediatheque

![Tests](https://github.com/MourtallaGueye/mini-projet-poo-Mourtalla-Gueye/actions/workflows/tests.yml/badge.svg)

Petite application Python (bibliothèque standard uniquement) de gestion d'une
médiathèque : documents (livres, DVD), adhérents, et prêts.

## Installation

    python -m pip install -r requirements.txt

## Lancer la démonstration

    python main.py

## Lancer les tests

    python -m pytest -q

### Résultat attendu

    .......                                                                 [100%]
    7 passed in 0.22s

## Structure du projet

    mini-projet-poo-Mourtalla-Gueye/
    ├── README.md
    ├── .gitignore
    ├── requirements.txt
    ├── mediatheque/
    │   ├── __init__.py
    │   ├── documents.py
    │   ├── adherent.py
    │   ├── mediatheque.py
    │   └── erreurs.py
    ├── tests/
    │   └── test_mediatheque.py
    └── main.py

## Auteur

Mourtalla Gueye