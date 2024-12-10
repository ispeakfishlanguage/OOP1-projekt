import datetime

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []  # Lista för att lagra interaktioner
        self.last_interaction = None  # Datum för senaste interaktionen

    def add_interaction(self, interaction_details):
        self.interactions.append(interaction_details)
        self.last_interaction = datetime.datetime.now()
        print(f"Interaktion tillagd för {self.name}: {interaction_details}")

    def calculate_days_since_last_interaction(self):
        if self.last_interaction is None:
            return None
        delta = datetime.datetime.now() - self.last_interaction
        return delta.days

    def is_inactive(self):
        """Returnerar True om kunden är inaktiv (över 30 dagar utan interaktion)."""
        if self.last_interaction is None:
            return True  # Ingen interaktion alls = inaktiv
        delta = datetime.datetime.now() - self.last_interaction
        return delta.days > 30
