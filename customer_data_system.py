from datetime import datetime
from customer import Customer

class CustomerDataSystem:
    """Ett system för att hantera kunddata och kundinteraktioner.

    Attribut:
        name: Systemets namn.
        customers (kunder): En lista över kunder i systemet."""
    def __init__(self, name):
        """Initialiserar systemet med ett namn och en tom lista för kunder."""
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        """Lägger till en ny kund om e-postadressen inte redan finns."""
        if any(customer.email == email for customer in self.customers):
            raise CustomerSystemError("En kund med denna e-postadress finns redan.")
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)

    def remove_customer(self, email):
        """Tar bort en kund baserat på e-postadress, eller kastar ett undantag om kunden inte finns."""
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
        raise CustomerSystemError(f"Ingen kund med e-postadress {email} hittades.")

    def update_customer_contact(self, email, phone=None, new_email=None):
        """Uppdaterar kundens telefonnummer och/eller e-postadress."""
        if phone is None and new_email is None:
            raise CustomerSystemError("Inget att uppdatera: Ange antingen telefonnummer eller ny e-postadress.")
        for customer in self.customers:
            if customer.email == email:
                if phone:
                    customer.phone = phone
                if new_email:
                    if any(c.email == new_email for c in self.customers):
                        raise CustomerSystemError("En kund med denna nya e-postadress finns redan.")
                    customer.email = new_email
                    break
        else:
            raise CustomerSystemError(f"Ingen kund med e-postadress {email} hittades.")

    def list_customers(self):
        """Skriver ut alla kunder i systemet."""
        return [
            f"- {customer.name} ({customer.email}, {customer.phone})"
            for customer in self.customers
        ]

    def list_inactive_customers(self):
        """Skriver ut alla kunder som är inaktiva (över 30 dagar utan interaktion)."""
        return [
            f"- {customer.name} ({customer.email}): "
            f"{'Aldrig haft interaktion' if not customer.interactions else (datetime.now() - customer.last_interaction).days} dagar inaktiv"
            for customer in self.customers if customer.is_inactive()
        ]

    def get_customer_details(self, email):
        """Returnerar detaljer om en kund baserat på e-postadress."""
        for customer in self.customers:
            if customer.email == email:
                return customer
        raise CustomerSystemError(f"Ingen kund med e-postadress {email} hittades.")

class CustomerSystemError(Exception):
    """An error that occurred in the customer data system."""
    def __init__(self, message):
        super().__init__(message)
