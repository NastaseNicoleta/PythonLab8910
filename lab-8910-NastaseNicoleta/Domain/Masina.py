from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Masina(Entitate):
    model: str
    anAchizitie: int
    nrKm: int
    inGarantie: str
    
