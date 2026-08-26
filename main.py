"""Programme de démonstration de la médiathèque."""

from mediatheque import Mediatheque, Livre, DVD, DocumentIndisponible


def main():
    mediatheque = Mediatheque("Mediatheque de Dakar")

    mediatheque.ajouter_document(
        Livre("L'Aventure ambigue", 1961, "L001",
              auteur="Cheikh Hamidou Kane", nb_pages=191)
    )
    mediatheque.ajouter_document(
        DVD("Camp de Thiaroye", 1988, "D001",
            realisateur="Sembene Ousmane", duree_min=147)
    )

    awa = mediatheque.inscrire("Awa Diop")

    pret = mediatheque.emprunter(awa.numero, "L001")
    print(pret)          # Livre "L'Aventure ambigue" (1961) - ... - a rendre sous 21 jours
    print(len(awa))      # 1

    try:
        mediatheque.emprunter(awa.numero, "L001")
    except DocumentIndisponible as err:
        print("Impossible :", err)

    print("\nRecherche 'aventure' :")
    for doc in mediatheque.rechercher("aventure"):
        print(" -", doc)

    print("\nDocuments disponibles :")
    for doc in mediatheque.documents_disponibles():
        print(doc)  # le meme appel, un affichage different : polymorphisme

    mediatheque.rendre(awa.numero, "L001")
    print("\nAprès restitution, len(awa) =", len(awa))


if __name__ == "__main__":
    main()