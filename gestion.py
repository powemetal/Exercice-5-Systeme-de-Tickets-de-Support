from ticket import Ticket


tickets = []

def creer_ticket(nom, sujet, priorite):
    nouveau_ticket = Ticket(nom, sujet, priorite)
    tickets.append(nouveau_ticket)

def afficher_tickets():
    for ticket in tickets:
        print(ticket)

def afficher_ticket_par_id(numero):
    for ticket in tickets:
        if ticket.numero == numero:
            return ticket

def mettre_a_jour(numero, nom=None, sujet=None, priorite=None):
    ticket = afficher_ticket_par_id(numero)
    if ticket is not None:
        if nom is not None:
            ticket.nom = nom
        if sujet is not None:
            ticket.sujet = sujet
        if priorite is not None:
            ticket.priorite = priorite
        print("Succes de la mise a jour des informations!")
    else:
        print("Erreur de la mise a jour des informations!")

def supprimer_ticket(numero):
    ticket = afficher_ticket_par_id(numero)
    if ticket is not None:
        tickets.remove(ticket)
        print("Ticket supprime!")
    else:
        print("Erreur de suppression")

# a = creer_ticket("to","tr","2")
# a = creer_ticket("fdds","qq","2")
# a = creer_ticket("dsf","ww","2")
# a = creer_ticket("555","ee","2")
# afficher_tickets()
# print(afficher_ticket_par_id(3))
# mettre_a_jour(3, "Toleen", "rien", "2")
# print(afficher_ticket_par_id(3))
# supprimer_ticket(3)
# afficher_tickets()