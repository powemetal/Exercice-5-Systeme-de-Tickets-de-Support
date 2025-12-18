class Ticket:
    num = 0
    def __init__(self, nom, sujet, priorite):
        Ticket.num += 1
        self.numero = Ticket.num
        self.nom = nom
        self.sujet = sujet
        self.priorite = priorite
        
    def __str__(self):
        return f"Ticket #{self.numero} nom={self.nom} sujet={self.sujet} priorite={self.priorite}"
    
# a = Ticket("Charles", "PROBLEME","1")
# b = Ticket("Dharles", "PROBLEME","1")
# c = Ticket("Eharles", "PROBLEME","1")
# d = Ticket("Fharles", "PROBLEME","1")

# print(d)