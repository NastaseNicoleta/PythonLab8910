import jsonpickle
from Domain.entitate import Entitate
from Repository.RepositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        '''
        citim din fisier
        :return:
        '''
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        '''
        scriem in fisier
        :return:
        '''
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati, indent=2))

    def read(self, idEntitate=None):
        '''
        cititm un obiect din fisier
        :param idEntitate:
        :return:
        '''
        self.entitati = self.__readFile()
        return super().read(idEntitate)

    def adauga(self, entitate: Entitate):
        '''
        adaugam un obiect in fisier
        :param entitate:
        :return:
        '''
        self.entitati = self.__readFile()
        super().adaugare(entitate)
        self.__writeFile()

    def sterge(self, idEntitate):
        '''
        stergem un obiect din fisier
        :param idEntitate:
        :return:
        '''
        self.entitati = self.__readFile()
        super().stergere(idEntitate)
        self.__writeFile()

    def modifica(self, entitate: Entitate):
        '''
        modificam un obiect din fisier
        :param entitate:
        :return:
        '''
        self.entitati = self.__readFile()
        super().modificare(entitate)
        self.__writeFile()
