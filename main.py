import datetime
from customer_data_system import CustomerDataSystem  # Importera systemklassen

# Skapa kunddatasystemet
system = CustomerDataSystem(name="CDD24")

# Steg 1: Lägg till några kunder
try:
    system.add_customer("Emma Andersson", "emma@example.com", "0701234567")
    system.add_customer("Jonas Eriksson", "jonas@example.com", "0707654321")
    system.add_customer("Lisa Sundberg", "lisa@example.com", "0705555555")
except ValueError as e:
    print(f"Fel vid tillägg av kund: {e}")

# Steg 2: Lista alla kunder
system.list_customers()

# Steg 3: Lägg till interaktioner
try:
    system.customers[0].add_interaction("Köpte ny produkt")
    system.customers[1].add_interaction("Frågade om support")
except IndexError as e:
    print(f"Fel vid tillägg av interaktion: {e}")

# Steg 4: Uppdatera en kunds kontaktinformation
try:
    system.update_customer_contact("emma@example.com", phone="0701112222", new_email="emma.andersson@example.com")
except (ValueError, KeyError) as e:
    print(f"Fel vid uppdatering av kund: {e}")

# Steg 5: Ta bort en kund
try:
    system.remove_customer("jonas@example.com")
except KeyError as e:
    print(f"Fel vid borttagning av kund: {e}")

# Steg 6: Lista inaktiva kunder
print("\nInitial lista av inaktiva kunder:")
system.list_inactive_customers()

# Simulera äldre interaktion (manuellt justera datum)
system.customers[0].last_interaction -= datetime.timedelta(days=40)

# Steg 7: Lista inaktiva kunder igen efter ändring
print("\nLista av inaktiva kunder efter datumjustering:")
system.list_inactive_customers()

# Steg 8: Försök lägga till en kund med en befintlig e-postadress
try:
    system.add_customer("Test Person", "emma.andersson@example.com", "0700000000")
except ValueError as e:
    print(f"Fel vid tillägg av kund: {e}")

# Steg 9: Försök ta bort en kund som inte existerar
try:
    system.remove_customer("icke.existerande@example.com")
except KeyError as e:
    print(f"Fel vid borttagning av kund: {e}")
