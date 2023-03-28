
from Domain.Masina import Masina


class MasinaValidator:
    def valideaza(self, masina: Masina):
        erori = []
        if masina.nrKm < 0:
            erori.append("Numarul de kilometri trebuie sa fie pozitiv!")
        if masina.anAchizitie < 0:
            erori.append("Anul achizitiei masinii trebuie sa fie pozitiv!")
        if masina.inGarantie not in ['da', 'nu']:
            erori.append("Stadiul garantiei este gresit!")
        if len(erori) > 0:
            raise ValueError(erori)
