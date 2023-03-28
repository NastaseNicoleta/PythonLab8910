from Domain.undoRedoOperation import UndoRedoOperation


class UndoRedoService:
    def __init__(self):
        self.__undoOperations: list[UndoRedoOperation] = []
        self.__redoOperations: list[UndoRedoOperation] = []

    def addUndoRedoOperation(self, undo_redo_operation: UndoRedoOperation):
        self.__undoOperations.append(undo_redo_operation)
        self.__redoOperations.clear()

    def deleteOperation(self):
        if self.__undoOperations:
            self.__undoOperations.pop()

    def undo(self):
        if self.__undoOperations:
            last_undo_operation = self.__undoOperations.pop()
            self.__redoOperations.append(last_undo_operation)
            last_undo_operation.doUndo()

    def redo(self):
        if self.__redoOperations:
            last_redo_operation = self.__redoOperations.pop()
            self.__undoOperations.append(last_redo_operation)
            last_redo_operation.doRedo()
