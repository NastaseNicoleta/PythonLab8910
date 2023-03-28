from dataclasses import dataclass
from datetime import date

from Domain.entitate import Entitate


@dataclass
class CardClient(Entitate):
    nume: str
    prenume: str
    CNP: str
    data_nasterii: date
    data_inregistrarii: date
