
from Domain.CardClient import CardClient


class CardClientValidator:
    def valideaza(self, card: CardClient):
        erori = []
        if int(card.CNP) < 0:
            erori.append("CNP-ul trebuie sa fie strict pozitiv!")
        lista = []
        for x in card.CNP:
            lista.append(x)
        if len(lista) != 13:
            erori.append("CNP-ul trebuie aiba 13 cifre!")
        if len(erori) > 0:
            raise ValueError(erori)
