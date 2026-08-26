"""Classe Mediatheque : orchestre documents, adhérents et prêts."""

import itertools

from .adherent import Adherent
from .erreurs import DocumentIndisponible, DocumentInconnu, TropDEmprunts


class Mediatheque:
    """Gère les documents, les adhérents et les emprunts."""

    def __init__(self, nom):
        self.nom = nom
        self._documents = {}       # code -> Document
        self._adherents = {}       # numero -> Adherent
        self._compteur = itertools.count(1)

    # --- gestion des documents et adhérents -----------------------------

    def ajouter_document(self, document):
        self._documents[document.code] = document

    def inscrire(self, nom):
        numero = next(self._compteur)
        adherent = Adherent(nom, numero)
        self._adherents[numero] = adherent
        return adherent

    def _document(self, code):
        try:
            return self._documents[code]
        except KeyError:
            raise DocumentInconnu(f"Aucun document avec le code {code!r}") from None

    def _adherent(self, numero):
        try:
            return self._adherents[numero]
        except KeyError:
            raise DocumentInconnu(f"Aucun adhérent avec le numéro {numero!r}") from None

    # --- prêts ------------------------------------------------------------

    def emprunter(self, numero, code):
        adherent = self._adherent(numero)
        document = self._document(code)

        if not document.disponible:
            raise DocumentIndisponible(
                f"Le document {code!r} est déjà emprunté"
            )
        if not adherent.peut_emprunter():
            raise TropDEmprunts(
                f"{adherent.nom} a déjà 3 emprunts en cours"
            )

        document.marquer_emprunte()
        adherent.ajouter_emprunt(document)
        return document

    def rendre(self, numero, code):
        adherent = self._adherent(numero)
        document = self._document(code)

        document.marquer_disponible()
        adherent.retirer_emprunt(document)
        return document

    # --- consultation -------------------------------------------------

    def rechercher(self, mot):
        mot = mot.lower()
        return [d for d in self._documents.values() if mot in d.titre.lower()]

    def documents_disponibles(self):
        return [d for d in self._documents.values() if d.disponible]

    def emprunts_de(self, numero):
        return self._adherent(numero).emprunts