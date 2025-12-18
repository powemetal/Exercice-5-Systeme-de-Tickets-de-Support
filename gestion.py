from ticket import Ticket

class GestionTicket:
    def __init__(self):
        self.tickets = []

    def creer_ticket(self, nom, sujet, priorite):
        nouveau_ticket = Ticket(nom, sujet, priorite)
        self.tickets.append(nouveau_ticket)
        return nouveau_ticket
    
    def lire_tickets(self):
        return self.tickets
    
    def mettre_a_jour(self, numero, nom=None, sujet=None, priorite=None):
        for ticket in self.tickets:
            if ticket.numero == numero:
                if nom is not None:
                    ticket.nom = nom
                if sujet is not None:
                    ticket.sujet = sujet
                if priorite is not None:
                    ticket.priorite = priorite
                return ticket
        return None


    def supprimer_ticket(self, numero):
        for ticket in self.tickets:
            if ticket.numero == numero:
                self.tickets.remove(ticket)
                return True
        return False
