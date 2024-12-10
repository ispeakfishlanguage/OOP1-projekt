from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Customer:
    """
    Representerar en enskild kund i systemet.

    Attribut:
        name: Namnet på kunden.
        email: Kundens e-postadress.
        phone (telefon): Kundens telefonnummer.
        interactions (interaktioner): En lista med interaktionsdetaljer.
        last_interaction (senaste interaktion): Datum och tid för den senaste interaktionen.
    """
    name: str
    email: str
    phone: str
    interactions: List[str] = field(default_factory=list)
    last_interaction: Optional[datetime] = field(default_factory=datetime.now)

    def add_interaction(self, interaction_details: str):
        """Lägger till en interaktion och uppdaterar den senaste interaktionstiden."""
        self.interactions.append(interaction_details)
        self.last_interaction = datetime.now()
        print(f"Interaktion tillagd för {self.name}: {interaction_details}")

    def calculate_days_since_last_interaction(self) -> Optional[int]:
        """Beräknar antalet dagar sedan den senaste interaktionen."""
        if self.last_interaction is None:
            return None
        delta = datetime.now() - self.last_interaction
        return delta.days

    def is_inactive(self) -> bool:
        """Kontrollerar om kunden är inaktiv.

        En kund är inaktiv om den senaste interaktionen skedde för mer än 30 dagar sedan."""
        if self.last_interaction is None:
            return True  # Ingen interaktion alls = inaktiv
        delta = datetime.now() - self.last_interaction
        return delta.days > 30
