from dataclasses import dataclass
from datetime import date, time

from Domain.entitate import Entitate


@dataclass
class Tranzactie(Entitate):
    idMasina: str
    idCardClient: str
    sumaPiese: float
    sumaManopera: float
    data: date
    ora: time
