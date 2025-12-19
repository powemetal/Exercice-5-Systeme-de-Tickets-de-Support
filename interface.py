# faire fonctions pour clear screen
import os
import gestion
from ticket import Ticket

def clear_screen():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux / macOS
    else:
        os.system("clear")

entete = ""

choix = ""
menu_principal = """
=== Bienvenue dans le systeme de gestion de tickets ===
1- Créer un Ticket
2- Gestion des Tickets
3- Sauvegarder les Tickets

Q- Quitter l'application"""


menu_gestion = """
-- Gestion des Tickets --
1- Voir les tickets
2- Voir un ticket
3- Changer l'etat d'un ticket
4- Supprimer un ticket

Q- Menu principal
"""
while True:
    choix = ""
    clear_screen()
    print(entete)
    print(menu_principal)
    choix = input("\nEntrez un choix: ").lower()
    if choix == "1":
        entete = "-- Creation d'un Ticket --"
        clear_screen()
        print(f"{entete}\n")
        nom, sujet, priorite = [input(prompt) for prompt in ("Entrez le nom de votre ticket: ", "Entrez le sujet de votre ticket: ", "Quelle est la prioritee?: ")]
        gestion.creer_ticket(nom, sujet, priorite)
        entete = f"Ticket: (#{Ticket.num} -Nom: {nom} -Sujet: {sujet} -Prioritée: {priorite}) créé"

        # gestion.creer_ticket(nom, sujet, priorite)

    if choix == "2":
        entete = ""
        while True:
            choix_gestion = ""
            clear_screen()
            print(entete)
            print(menu_gestion)
            choix_gestion = input("\nEntrez un choix: ").lower()
            if choix_gestion == "1":
                clear_screen()
                entete = "-- Voir les tickets --\n"
                gestion.afficher_tickets()
                input("\nAppuyez sur entree pour continuer")

            if choix_gestion == "2":
                clear_screen()
                entete = "-- Voir un ticket --"
                id_ticket = input("Entrez le numero du ticket: ")
                print(f"\n{gestion.afficher_ticket_par_id(int(id_ticket))}")
                input("\nAppuyez sur entree pour continuer")


            if choix_gestion == "3":
                entete = "-- Modifier un ticket --"

            if choix_gestion == "4":
                entete = "Supprimer un ticket"

            if choix_gestion == "q":
                entete = ""
            
            else:
                entete = "Votre choix est invalide, entrez un chiffre de 1 à 4 ou q-Q pour quitter"
                break


    if choix == "3":
        entete = "Sauvegarder les Tickets"

    if choix == "q":
        break

    else:
        entete = "Votre choix est invalide, entrez un chiffre de 1 à 3 ou q-Q pour quitter"

print("\nAu revoir")
