# Mediatheque

Petite application Python (bibliothèque standard uniquement) de gestion d'une
médiathèque : documents (livres, DVD), adhérents, et prêts.

La conception met l'accent sur les quatre piliers de la programmation orientée
objet : encapsulation, héritage, polymorphisme et abstraction.

## Structure du projet

    mini-projet-poo-Mourtalla-Gueye/
    ├── README.md
    ├── .gitignore
    ├── conftest.py            # permet a pytest de trouver le package mediatheque
    ├── mediatheque/
    │   ├── __init__.py
    │   ├── documents.py       # Document (abstraite), Livre, DVD
    │   ├── adherent.py        # Adherent
    │   ├── mediatheque.py     # Mediatheque (gestion des prets)
    │   └── erreurs.py         # Exceptions personnalisees
    ├── tests/
    │   └── test_mediatheque.py
    └── main.py                 # Programme de demonstration

## Lancer la démonstration

    python main.py

## Lancer les tests

    pytest -q

Un fichier `conftest.py` vide est présent à la racine : il permet à pytest de
détecter automatiquement le package `mediatheque` lors de l'exécution des
tests, quel que soit le système d'exploitation.

## Auteur

Mourtalla Gueye