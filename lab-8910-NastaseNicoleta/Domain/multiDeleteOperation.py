from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiDeleteOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecte_sterse):
        self.repository = repository
        self.obiecte_sterse = obiecte_sterse

    def doUndo(self):
        for entitate in self.obiecte_sterse:
            self.repository.adaugare(entitate)

    def doRedo(self):
        for entitate in self.obiecte_sterse:
            self.repository.stergere(entitate.id_entitate)
