from Domain.tranzactie import Tranzactie


class TranzactieValidator:
    def valideaza(self, tranzactie: Tranzactie):
        erori = []
        if int(tranzactie.idMasina) < 0:
            erori.append("Id-ul masinii trebuie sa fie pozitiv!")
        if tranzactie.sumaPiese < 0:
            erori.append("Suma pieselor trebuie sa fie pozitiva!")
        if tranzactie.sumaManopera < 0:
            erori.append("Suma manoperei trebuie sa fie pozitiva!")
        if len(erori) > 0:
            raise ValueError(erori)
