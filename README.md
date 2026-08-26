# Mediatheque

Petite application Python (bibliothèque standard uniquement) de gestion d'une
médiathèque : documents (livres, DVD), adhérents, et prêts.

La conception met l'accent sur les quatre piliers de la programmation orientée
objet : encapsulation, héritage, polymorphisme et abstraction.

## Structure du projet

    mini-projet-poo-Mourtalla-Gueye/
    ├── README.md
    ├── .gitignore
    ├── mediatheque/
    │   ├── __init__.py
    │   ├── documents.py      # Document (abstraite), Livre, DVD
    │   ├── adherent.py       # Adherent
    │   ├── mediatheque.py    # Mediatheque (gestion des prets)
    │   └── erreurs.py        # Exceptions personnalisees
    ├── tests/
    │   └── test_mediatheque.py
    └── main.py                # Programme de demonstration

## Lancer la démonstration

    python main.py

## Lancer les tests

    pytest -q

Si cette commande ne trouve pas le module `mediatheque` (erreur
`ModuleNotFoundError`, cela peut arriver selon la configuration Python de
certaines machines Windows), utilisez plutôt :

    python -m pytest -q

Les deux commandes lancent les mêmes 7 tests ; la seconde force Python à
ajouter le dossier courant au chemin d'import, ce que `pytest` seul ne fait
pas toujours selon l'environnement.

## Auteur

Mourtalla Gueye