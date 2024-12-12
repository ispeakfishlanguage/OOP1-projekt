# Kundhanteringssystem
Detta projekt är ett kundhanteringssystem byggt i Python. Systemet tillåter hantering av kundprofiler och interaktioner, inklusive att lägga till, uppdatera och ta bort kunder, samt identifiera inaktiva kunder.

## Projektstruktur
````
OOP1-projekt/
├── customer.py                     # Definierar Customer-klassen för individuella kunder.
├── customer_data_system.py         # Definierar CustomerDataSystem för hantering av kunddata.
├── test_customer_data_system.py    # Enhetstester för systemet.
├── main.py                         # Program som demonstrerar funktionalitet.
├── README.md
└── LICENSE 
````

## Funktioner
* Lägga till, uppdatera och ta bort kunder.
* Lägga till interaktioner och hålla reda på senaste interaktion.
* Identifiera inaktiva kunder (ingen interaktion på över 30 dagar).
* Hantering av undantag med en custom exception (`CustomerSystemError`).

## Krav
Python 3.8 eller senare.

## Installation
1. Klona eller ladda ner projektet:
````
git clone <https://github.com/ispeakfishlanguage/OOP1-projekt>
cd projekt
````

2. Skapa och aktivera en virtuell miljö (valfritt):
````
python -m venv .venv
source .venv/bin/activate  # På Windows: .venv\Scripts\activate
````

3. Installera beroenden om några krävs (inga specifika i detta projekt).

## Köra enhetstester
För att köra enhetstester och verifiera funktionalitet:
````
python -m unittest test_customer_data_system.py
````
Exempel på resultat:
````
Ran 8 tests in 0.001s

OK
````
## Exempel på användning
Lägg till en ny kund:
````
system.add_customer("Anna Ahlberg", "anna@example.com", "0701234567")

````
Lista alla kunder:
````
system.list_customers()
````
Uppdatera en kunds kontaktinformation:
````
system.update_customer_contact("anna@example.com", phone="0707654321", new_email="anna.ahlberg@example.com")
````
