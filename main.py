import datetime
from customer_data_system import CustomerDataSystem, CustomerSystemError  # Importera system och custom exception

# Skapa kunddatasystemet
system = CustomerDataSystem(name="CDD24")

# Steg 1: Lägg till några kunder
clients = [
    ("Emma Andersson", "emma@example.com", "0701234567"),
    ("Jonas Eriksson", "jonas@example.com", "0707654321"),
    ("Lisa Sundberg", "lisa@example.com", "0705555555")
]
try:
    for client in clients:
        system.add_customer(*client)
        print(f"Kund med namn {client[0]} har lagts till.")
except CustomerSystemError as e:
    print(f"Systemfel: {e}")

# Steg 2: Lista alla kunder
print("Kunder i systemet:")
for customer in system.list_customers():
    print(customer)

# Steg 3: Lägg till interaktioner
try:
    system.customers[0].add_interaction("Köpte ny produkt")
    print(f"{system.customers[0].interactions[-1]} {system.customers[0].last_interaction}")
    system.customers[1].add_interaction("Frågade om support")
    print(f"{system.customers[1].interactions[-1]} {system.customers[1].last_interaction}")
except IndexError as e:
    print(f"Fel vid tillägg av interaktion: {e}")

# Steg 4: Uppdatera en kunds kontaktinformation
try:
    system.update_customer_contact("lisa@example.com", phone="0702223333", new_email="new.lisa@example.com")
    customer = system.get_customer_details("new.lisa@example.com")
    print(f"Kundens kontaktinformation har uppdaterats för {customer.name}.")
except CustomerSystemError as e:
    print(f"Systemfel: {e}")

# Steg 5: Ta bort en kund
try:
    email = "jonas@example.com"
    system.remove_customer("jonas@example.com")
    print(f"Kunden med e-postadress {email} har tagits bort.")
except CustomerSystemError as e:
    print(f"Systemfel: {e}")

# Steg 6: Lista inaktiva kunder
print("Initial lista av inaktiva kunder:")
for inactive in system.list_inactive_customers():
    print(inactive)

# Simulera äldre interaktion (manuellt justera datum)
try:
    system.customers[0].last_interaction -= datetime.timedelta(days=40)
except IndexError as e:
    print(f"Fel vid justering av datum: {e}")

# Steg 7: Lista inaktiva kunder igen efter datumjustering
print("Lista av inaktiva kunder efter datumjustering:")
for inactive in system.list_inactive_customers():
    print(inactive)

# Steg 8: Försök lägga till en kund med en befintlig e-postadress
try:
    system.add_customer("Test Person", "emma@example.com", "0700000000")
except CustomerSystemError as e:
    print(f"Systemfel vid tillägg av kund: {e}")

# Steg 9: Försök ta bort en kund som inte existerar
try:
    system.remove_customer("none@example.com")
except CustomerSystemError as e:
    print(f"Systemfel vid borttagning av kund: {e}")
