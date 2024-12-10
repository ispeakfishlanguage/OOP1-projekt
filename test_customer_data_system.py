import unittest
import datetime
from customer_data_system import CustomerDataSystem, CustomerSystemError
from contextlib import redirect_stdout
import io

class TestCustomerDataSystem(unittest.TestCase):

    def setUp(self):
        """Ställ in CustomerDataSystem för varje test."""
        self.system = CustomerDataSystem(name="CDD24")
        # Undertrycka utskrift under setup
        with io.StringIO() as buf, redirect_stdout(buf):
            self.system.add_customer("Emma Andersson", "emma@example.com", "0701234567")
            self.system.add_customer("Jonas Eriksson", "jonas@example.com", "0707654321")
            self.system.add_customer("Lisa Sundberg", "lisa@example.com", "0705555555")

    def test_add_customer(self):
        """Test: lägga till en ny kund."""
        self.system.add_customer("New Customer", "new@example.com", "0709999999")
        self.assertEqual(len(self.system.customers), 4)

    def test_add_customer_duplicate_email(self):
        """Test: lägga till en kund med en duplicerad e-postadress."""
        with self.assertRaises(CustomerSystemError):
            self.system.add_customer("Duplicate", "emma@example.com", "0700000000")

    def test_remove_customer(self):
        """Test: ta bort en kund."""
        self.system.remove_customer("jonas@example.com")
        self.assertEqual(len(self.system.customers), 2)
        with self.assertRaises(CustomerSystemError):
            self.system.remove_customer("jonas@example.com")  # Kund redan borttagen

    def test_remove_nonexistent_customer(self):
        """Test: ta bort en obefintlig kund."""
        with self.assertRaises(CustomerSystemError) as context:
            self.system.remove_customer("nonexistent@example.com")
        self.assertEqual(str(context.exception), "Ingen kund med e-postadress nonexistent@example.com hittades.")

    def test_update_customer_contact(self):
        """Test: uppdatering av kundens kontaktuppgifter."""
        self.system.update_customer_contact("emma@example.com", phone="0702223333", new_email="new.emma@example.com")
        customer = self.system.get_customer_details("new.emma@example.com")
        self.assertEqual(customer.phone, "0702223333")

    def test_update_customer_contact_duplicate_email(self):
        """Test: uppdatering av kund med en duplicerad e-postadress."""
        with self.assertRaises(CustomerSystemError):
            self.system.update_customer_contact("emma@example.com", new_email="jonas@example.com")

    def test_list_inactive_customers(self):
        """Test: lista inaktiva kunder."""
        # Simulera inaktivitet
        self.system.customers[0].last_interaction -= datetime.timedelta(days=40)
        inactive_customers = [customer for customer in self.system.customers if customer.is_inactive()]
        self.assertEqual(len(inactive_customers), 1)
        self.assertEqual(inactive_customers[0].name, "Emma Andersson")

    def test_get_customer_details(self):
        """Test: hämta kundinformation."""
        customer = self.system.get_customer_details("emma@example.com")
        self.assertEqual(customer.name, "Emma Andersson")
        with self.assertRaises(CustomerSystemError):
            self.system.get_customer_details("nonexistent@example.com")

if __name__ == "__main__":
    unittest.main()