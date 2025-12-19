
import json

def sauvegarder(gestion, fichier="tickets.json"):
    tickets = []

      # Transformer les tickets en dictionnaires
    for t in gestion.tickets:
        tickets.append({
            "numero": t.numero,
            "nom": t.nom,
            "sujet": t.sujet,
            "priorite": t.priorite
        })

    # Ouvrir le fichier en écriture
    f = open(fichier, "w")
    json.dump(tickets, f, indent=4)
    f.close()


def charger(gestion, fichier="tickets.json"):
        # Ouvrir le fichier en lecture
    f = open(fichier, "r")
    tickets = json.load(f)
    f.close()

        # Recréer les tickets
    for t in tickets:
        gestion.creer_ticket(
            t["nom"],
            t["sujet"],
            t["priorite"]
        )
