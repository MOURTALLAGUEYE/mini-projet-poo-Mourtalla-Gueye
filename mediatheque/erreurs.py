"""Exceptions personnalisées de la médiathèque."""


class MediathequeError(Exception):
    """Classe de base pour toutes les erreurs de la médiathèque."""


class DocumentIndisponible(MediathequeError):
    """Levée quand on tente d'emprunter un document déjà prêté."""


class TropDEmprunts(MediathequeError):
    """Levée quand un adhérent dépasse la limite de 3 emprunts."""


class DocumentInconnu(MediathequeError):
    """Levée quand un code document ou un numéro d'adhérent n'existe pas."""