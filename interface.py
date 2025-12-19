menu_principal = """
=== Bienvenue dans le systeme de gestion de tickets ===
1- Créer un Ticket
2- Gestion des Tickets
3- Sauvegarder les Tickets
4- Charger les Tickets

Q- Quitter l'application"""


menu_gestion = """
-- Gestion des Tickets --
1- Voir les tickets
2- Voir un ticket
3- Mettre a jour un ticket
4- Supprimer un ticket

Q- Menu principal
"""

#Au départ j'ai fait la navigation de l'interface ici au lieu du main
# while True:
#     choix = ""
#     clear_screen()
#     print(entete)
#     print(menu_principal)
#     choix = input("\nEntrez un choix: ").lower()
#     if choix == "1":
#         entete = "-- Creation d'un Ticket --"
#         clear_screen()
#         print(f"{entete}\n")
#         nom, sujet, priorite = "", "", ""
#         while nom == "":
#             clear_screen()
#             nom = input("Entrez le nom de votre ticket: ")
#         while sujet == "":
#             clear_screen()
#             sujet = input("Entrez le sujet de votre ticket: ")
#         while priorite == "":
#             clear_screen()
#             priorite = input("Quelle est la prioritee?: ")
#         gestion.creer_ticket(nom, sujet, priorite)
#         entete = f"Ticket: (#{Ticket.num} -Nom: {nom} -Sujet: {sujet} -Prioritée: {priorite}) créé"

#         # gestion.creer_ticket(nom, sujet, priorite)

#     if choix == "2":
#         entete = ""
#         while True:
            
#             clear_screen()
#             print(entete)
#             print(menu_gestion)
#             choix_gestion = input("\nEntrez un choix: ").lower()
#             if choix_gestion == "1":
#                 clear_screen()
#                 print("-- Voir les tickets --\n")
#                 gestion.afficher_tickets()
#                 input("\nAppuyez sur entree pour continuer")
#                 entete = ""
#                 continue

#             if choix_gestion == "2":
#                 clear_screen()
#                 print("-- Voir un ticket --\n")
#                 id_ticket = input("Entrez le numero du ticket: ")
#                 print(f"\n{gestion.afficher_ticket_par_id(int(id_ticket))}")
#                 input("\nAppuyez sur entree pour continuer")
#                 entete = ""
#                 continue


#             if choix_gestion == "3":
#                 clear_screen()
#                 id_ticket = None
#                 while not id_ticket:
#                     clear_screen()
#                     print("-- Mettre a jour un ticket --\n")
#                     input_id_ticket = input("Entrez le numero du ticket a mettre a jour: ")
#                     if input_id_ticket.isdigit():
#                         id_ticket = int(input_id_ticket.strip())
#                     else:
#                         print("Ceci n'est pas une Entree valide")
#                         input("Appuyez sur entree pour continuer")

#                 if gestion.afficher_ticket_par_id(id_ticket) :
#                     clear_screen()
#                     print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                     print("Voulez vous modifier ce ticket?")
#                     decision = input("Entrez oui pour continuer: ").lower()
#                     if decision == "oui":
#                         clear_screen()
#                         print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                         print("Quelle partie du ticket voulez vous modifier?\n")
#                         partie_a_modifier = input("Entrez Votre Choix: N pour nom - S pour sujet - P pour prioritée: ").lower()
#                         ticket_a_modifier = gestion.afficher_ticket_par_id(int(id_ticket))
#                         nom = ticket_a_modifier.nom
#                         sujet = ticket_a_modifier.sujet
#                         priorite = ticket_a_modifier.priorite
#                         ticket_modified = 0
#                         if partie_a_modifier == "n":
#                             input_nom = ""
#                             while input_nom == "":
#                                 clear_screen()
#                                 print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                                 input_nom = input("Entrez le nouveau nom: ")
#                                 ticket_modified = 1
#                                 if input_nom:
#                                     nom = input_nom
                            
#                         elif partie_a_modifier == "s":
#                             input_sujet = ""
#                             while input_sujet == "":
#                                 clear_screen()
#                                 print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                                 input_sujet = input("Entrez le nouveau sujet: ")
#                                 ticket_modified = 1
#                                 if input_sujet:
#                                     sujet = input_sujet
                            
#                         elif partie_a_modifier == "p":
#                             input_priorite = ""
#                             while input_priorite == "":
#                                 clear_screen()
#                                 print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                                 input_priorite = input("Entrez la nouvelle prioritée: ")
#                                 ticket_modified = 1
#                                 if input_priorite:
#                                     priorite = input_priorite
                            
#                         else:
#                             entete = "Ce choix est invalide"

#                         if ticket_modified:
#                             clear_screen()
#                             print("Acceptez vous les changements?: \n")
#                             print(f"Ancien ticket:  {gestion.afficher_ticket_par_id(int(id_ticket))}")
#                             print(f"Nouveau ticket: Ticket #{ticket_a_modifier.numero} nom={nom} sujet={sujet} priorite={priorite}\n")
#                             confirmation_changements = input("Entrez oui pour confirmer les changements: ").lower()
#                             if confirmation_changements == "oui":
#                                 clear_screen()
#                                 gestion.mettre_a_jour(int(id_ticket), nom, sujet, priorite)
#                                 print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                                 input("Appuyez sur enter pour continuer")
#                             else:
#                                 clear_screen()
#                                 print(f"{gestion.afficher_ticket_par_id(int(id_ticket))}\n")
#                                 input("Changements annulés, appuyez sur enter pour continuer")

#                 else:
#                     entete = (f"Le ticket #{id_ticket} n'existe pas")
#                 continue

#             if choix_gestion == "4":
#                 entete = "Supprimer un ticket"
#                 continue
#             if choix_gestion == "q":
#                 entete = ""
#                 break
#             else:
#                 entete = "Votre choix est invalide, entrez un chiffre de 1 à 4 ou q-Q pour quitter"
#         continue        


#     if choix == "3":
#         entete = "Sauvegarder les Tickets"

#     if choix == "q":
#         break

#     else:
#         entete = "Votre choix est invalide, entrez un chiffre de 1 à 3 ou q-Q pour quitter"

# print("\nAu revoir")
