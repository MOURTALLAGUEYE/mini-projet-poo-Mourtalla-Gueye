"""Package mediatheque : expose les classes principales."""

from .documents import Document, Livre, DVD
from .adherent import Adherent
from .mediatheque import Mediatheque
from .erreurs import (
    MediathequeError,
    DocumentIndisponible,
    TropDEmprunts,
    DocumentInconnu,
)

__all__ = [
    "Document",
    "Livre",
    "DVD",
    "Adherent",
    "Mediatheque",
    "MediathequeError",
    "DocumentIndisponible",
    "TropDEmprunts",
    "DocumentInconnu",
]