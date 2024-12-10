import datetime
from customer import Customer  # Importera kundklassen (om direkt behövs)

class CustomerDataSystem:
    def __init__(self, name):
        """Initialiserar systemet med ett namn och en tom lista för kunder."""
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        """Lägger till en ny kund om e-postadressen inte redan finns."""
        if any(customer.email == email for customer in self.customers):
            raise ValueError("En kund med denna e-postadress finns redan.")
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"Ny kund med namn {name} har lagts till.")

    def remove_customer(self, email):
        """Tar bort en kund baserat på e-postadress, eller kastar ett undantag om kunden inte finns."""
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print(f"Kunden med e-postadress {email} har tagits bort.")
                return
        raise KeyError(f"Ingen kund med e-postadress {email} hittades.")

    def update_customer_contact(self, email, phone=None, new_email=None):
        """Uppdaterar kundens telefonnummer och/eller e-postadress."""
        for customer in self.customers:
            if customer.email == email:
                if phone:
                    customer.phone = phone
                if new_email:
                    if any(c.email == new_email for c in self.customers):
                        raise ValueError("En kund med denna nya e-postadress finns redan.")
                    customer.email = new_email
                print(f"Kundens kontaktinformation har uppdaterats.")
                return
        raise KeyError(f"Ingen kund med e-postadress {email} hittades.")

    def list_customers(self):
        """Skriver ut alla kunder i systemet."""
        print(f"Kunder i {self.name}:")
        for customer in self.customers:
            print(f"- {customer.name} ({customer.email}, {customer.phone})")

    def is_inactive(self):
        """Returnerar True om kunden är inaktiv (över 30 dagar utan interaktion)."""
        if self.last_interaction is None:
            return True  # Ingen interaktion alls = inaktiv
        delta = datetime.datetime.now() - self.last_interaction
        return delta.days > 30

    def list_inactive_customers(self):
        """Skriver ut alla kunder som är inaktiva (över 30 dagar utan interaktion)."""
        print("Inaktiva kunder (över 30 dagar utan interaktion):")
        for customer in self.customers:
            if customer.is_inactive():
                days_inactive = (
                    None if customer.last_interaction is None
                    else (datetime.datetime.now() - customer.last_interaction).days
                )
                print(f"- {customer.name} ({customer.email}): {days_inactive} dagar inaktiv")