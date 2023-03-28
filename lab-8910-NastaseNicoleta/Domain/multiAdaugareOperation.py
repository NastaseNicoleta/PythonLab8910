from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiAdaugareOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecteAdaugate):
        self.__repository = repository
        self.__obiecteAdaugate = obiecteAdaugate

    def doUndo(self):
        for entitate in self.__obiecteAdaugate:
            self.__repository.stergere(entitate.id_entitate)

    def doRedo(self):
        for entitate in self.__obiecteAdaugate:
            self.__repository.adaugare(entitate)
