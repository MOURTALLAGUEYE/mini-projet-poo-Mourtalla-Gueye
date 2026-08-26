"""Classe Adherent."""

LIMITE_EMPRUNTS = 3


class Adherent:
    """Un adhérent de la médiathèque et ses emprunts en cours."""

    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero
        self._emprunts = []

    @property
    def emprunts(self):
        return list(self._emprunts)

    def peut_emprunter(self):
        return len(self._emprunts) < LIMITE_EMPRUNTS

    def ajouter_emprunt(self, document):
        self._emprunts.append(document)

    def retirer_emprunt(self, document):
        self._emprunts.remove(document)

    def __len__(self):
        return len(self._emprunts)

    def __str__(self):
        return f"{self.nom} (n°{self.numero}) - {len(self)} emprunt(s) en cours"