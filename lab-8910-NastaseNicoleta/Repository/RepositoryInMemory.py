from Repository.repository import Repository
from Domain.entitate import Entitate


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, idEntitate=None):
        if idEntitate is None:
            return list(self.entitati.values())

        if idEntitate in self.entitati:
            return self.entitati[idEntitate]
        else:
            return None

    def adaugare(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate

    def stergere(self, idEntitate: str):
        if self.read(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        del self.entitati[idEntitate]

    def modificare(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate
