from typing import Protocol

from Domain.entitate import Entitate


class Repository(Protocol):
    def read(self, idEntitate=None):
        ...

    def adaugare(self, entitate: Entitate):
        ...

    def stergere(self, idEntitate: str):
        ...

    def modificare(self, entitate: Entitate):
        ...
