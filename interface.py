# faire fonctions pour clear screen
import os

def clear_screen():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux / macOS
    else:
        os.system("clear")

dernier_message = ""

choix = ""
menu_principal = """
=== Bienvenue dans le systeme de gestion de tickets ===
1- Créer un Ticket
2- Gestion des Tickets
3- Sauvegarder les Tickets
Q- Quitter"""


menu_gestion = """
-- Gestion des Tickets --
1- Voir les tickets
2- Voir un ticket
3- Changer l'etat d'un ticket
4- Supprimer un ticket
Q- Quitter
"""
while True:
    choix = ""
    clear_screen()
    print(dernier_message)
    print(menu_principal)
    choix = input("\nEntrez un choix: ").lower()
    if choix == "1":
        dernier_message = "Creation d'un Ticket" #creation d'un ticket

    if choix == "2":
        dernier_message = ""
        while True:
            choix_gestion = ""
            clear_screen()
            print(dernier_message)
            print(menu_gestion)
            choix_gestion = input("\nEntrez un choix: ").lower()
            if choix_gestion == "1":
                dernier_message = "Voir les tickets"

            if choix_gestion == "2":
                dernier_message = "Voir un ticket"

            if choix_gestion == "3":
                dernier_message = "Changer l'etat d'un ticket"

            if choix_gestion == "4":
                dernier_message = "Supprimer un ticket"

            if choix_gestion == "q":
                dernier_message = ""
                break


    if choix == "3":
        dernier_message = "Sauvegarder les Tickets"

    if choix == "q":
        break

print("\nAu revoir")
