from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiUpdateOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecte_noi_modificate,
                 obiecte_vechi_modificate):
        self.repository = repository
        self.obiecte_noi_modificate = obiecte_noi_modificate
        self.obiecte_vechi_modificate = obiecte_vechi_modificate

    def do_undo(self):
        for entitate in self.obiecte_vechi_modificate:
            self.repository.modificare(entitate)

    def do_redo(self):
        for entitate in self.obiecte_noi_modificate:
            self.repository.modificare(entitate)
