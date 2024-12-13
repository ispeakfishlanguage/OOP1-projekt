import unittest
from datetime import datetime, timedelta
from customer_data_system import CustomerDataSystem, CustomerSystemError
from customer import Customer

class TestCustomerDataSystem(unittest.TestCase):

    def setUp(self):
        """Skapar ett nytt CustomerDataSystem och lägger till exempeldata för varje test."""
        self.system = CustomerDataSystem(name="Kundsystem")
        self.system.add_customer("Anna Andersson", "anna@example.com", "0701234567")
        self.system.add_customer("Lisa Sundberg", "lisa@example.com", "0707654321")

    def test_add_customer(self):
        """Testar att lägga till en ny kund."""
        self.system.add_customer("Jonas Eriksson", "jonas@example.com", "0709999999")
        self.assertEqual(len(self.system.customers), 3)

    def test_add_customer_duplicate_email(self):
        """Testar att lägga till en kund med en e-postadress som redan finns."""
        with self.assertRaises(CustomerSystemError):
            self.system.add_customer("Duplicate", "anna@example.com", "0708888888")

    def test_remove_customer(self):
        """Testar att ta bort en kund."""
        self.system.remove_customer("anna@example.com")
        self.assertEqual(len(self.system.customers), 1)
        with self.assertRaises(CustomerSystemError):
            self.system.remove_customer("anna@example.com")  # Försöker ta bort en kund som inte längre finns

    def test_remove_nonexistent_customer(self):
        """Testar att ta bort en obefintlig kund."""
        with self.assertRaises(CustomerSystemError) as context:
            self.system.remove_customer("nonexistent@example.com")
        self.assertEqual(str(context.exception), "Ingen kund med e-postadress nonexistent@example.com hittades.")

    def test_update_customer_contact(self):
        """Testar att uppdatera en kunds kontaktinformation."""
        self.system.update_customer_contact("lisa@example.com", phone="0702223333", new_email="new.lisa@example.com")
        customer = self.system.get_customer_details("new.lisa@example.com")
        self.assertEqual(customer.phone, "0702223333")
        self.assertEqual(customer.email, "new.lisa@example.com")

    def test_update_customer_contact_duplicate_email(self):
        """Testar att uppdatera en kunds e-postadress till en som redan finns."""
        with self.assertRaises(CustomerSystemError):
            self.system.update_customer_contact("lisa@example.com", new_email="anna@example.com")

    def test_list_customers(self):
        """Testar att lista alla kunder."""
        customers = self.system.list_customers()
        self.assertEqual(len(customers), 2)
        self.assertIn("- Anna Andersson (anna@example.com, 0701234567)", customers)
        self.assertIn("- Lisa Sundberg (lisa@example.com, 0707654321)", customers)

    def test_list_customers_after_update(self):
        """Testar att list_customers fungerar efter uppdatering av en kunds kontaktinformation."""
        self.system.update_customer_contact("lisa@example.com", phone="0703334444", new_email="updated.lisa@example.com")
        customers = self.system.list_customers()
        self.assertIn("- Lisa Sundberg (updated.lisa@example.com, 0703334444)", customers)

    def test_list_inactive_customers(self):
        """Testar att lista inaktiva kunder."""
        # Simulera att Anna har varit inaktiv i 40 dagar
        anna = self.system.get_customer_details("anna@example.com")
        anna.last_interaction = datetime.now() - timedelta(days=40)
        lisa = self.system.get_customer_details("lisa@example.com")
        lisa.last_interaction = datetime.now()
        inactive_customers = self.system.list_inactive_customers()

        # Validera objekt som returneras
        self.assertEqual(len(inactive_customers), 1)
        self.assertEqual(inactive_customers[0].name, "Anna Andersson")
        self.assertEqual(inactive_customers[0].calculate_days_since_last_interaction(), 40)


    def test_empty_customer_list(self):
        """Testar hantering av en tom kundlista."""
        empty_system = CustomerDataSystem(name="Tomt System")
        customers = empty_system.list_customers()
        self.assertEqual(len(customers), 0)
        inactive_customers = empty_system.list_inactive_customers()
        self.assertEqual(len(inactive_customers), 0)

    def test_get_customer_details(self):
        """Testar att hämta detaljer om en kund."""
        customer = self.system.get_customer_details("anna@example.com")
        self.assertEqual(customer.name, "Anna Andersson")
        self.assertEqual(customer.email, "anna@example.com")
        with self.assertRaises(CustomerSystemError):
            self.system.get_customer_details("nonexistent@example.com")

if __name__ == "__main__":
    unittest.main()
