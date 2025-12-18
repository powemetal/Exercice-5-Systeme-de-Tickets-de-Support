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
    
    def lire_ticket_par_id(self, numero):
        for ticket in self.tickets:
            if ticket.numero == numero:
                return ticket
        return None
    
    def mettre_a_jour(self, numero, nom=None, sujet=None, priorite=None):
        ticket = self.lire_ticket_par_id(numero)
        if ticket is not None:
            if nom is not None:
                ticket.nom = nom
            if sujet is not None:
                ticket.sujet = sujet
            if priorite is not None:
                ticket.priorite = priorite
            return ticket
        return None


    def supprimer_ticket(self, numero):
        ticket = self.lire_ticket_par_id(numero)
        if ticket is not None:
            self.tickets.remove(ticket)
            return True
        return False
