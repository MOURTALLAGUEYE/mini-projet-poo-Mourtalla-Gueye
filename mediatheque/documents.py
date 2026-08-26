"""Classes Document (abstraite), Livre et DVD."""

from abc import ABC, abstractmethod


class Document(ABC):
    """Classe de base abstraite pour tout document de la médiathèque."""

    def __init__(self, titre, annee, code):
        self._titre = titre
        self.annee = annee
        self._code = code
        self._disponible = True

    @property
    def titre(self):
        return self._titre

    @property
    def code(self):
        return self._code

    @property
    def disponible(self):
        return self._disponible

    def marquer_emprunte(self):
        """Marque le document comme emprunté (utilisé par Mediatheque)."""
        self._disponible = False

    def marquer_disponible(self):
        """Marque le document comme rendu (utilisé par Mediatheque)."""
        self._disponible = True

    @abstractmethod
    def duree_pret(self):
        """Nombre de jours de prêt autorisé pour ce type de document."""
        raise NotImplementedError

    def __str__(self):
        statut = "disponible" if self._disponible else "emprunté"
        return f'"{self._titre}" ({self.annee}) - {statut}'

    def __eq__(self, other):
        if not isinstance(other, Document):
            return NotImplemented
        return self._code == other._code

    def __hash__(self):
        return hash(self._code)


class Livre(Document):
    """Un livre : prêté pour 21 jours."""

    def __init__(self, titre, annee, code, auteur, nb_pages):
        super().__init__(titre, annee, code)
        self.auteur = auteur
        self.nb_pages = nb_pages

    def duree_pret(self):
        return 21

    def __str__(self):
        base = super().__str__()
        return (
            f'Livre {base} - {self.auteur}, {self.nb_pages} pages '
            f'- à rendre sous {self.duree_pret()} jours'
        )


class DVD(Document):
    """Un DVD : prêté pour 7 jours."""

    def __init__(self, titre, annee, code, realisateur, duree_min):
        super().__init__(titre, annee, code)
        self.realisateur = realisateur
        self.duree_min = duree_min

    def duree_pret(self):
        return 7

    def __str__(self):
        base = super().__str__()
        return (
            f'DVD {base} - réalisé par {self.realisateur}, {self.duree_min} min '
            f'- à rendre sous {self.duree_pret()} jours'
        )