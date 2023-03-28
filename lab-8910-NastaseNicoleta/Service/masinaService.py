from datetime import datetime
from random import choice, randint

from Domain.Masina import Masina
from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.masinaValidator import MasinaValidator
from Domain.modificareOperation import MultiUpdateOperation
from Domain.multiAdaugareOperation import MultiAdaugareOperation
from Repository.repositoryJson import RepositoryJson
from Service.undoRedoService import UndoRedoService


class MasinaService:
    def __init__(self, masinaRepository: RepositoryJson,
                 masinaValidator: MasinaValidator,
                 undoRedoService: UndoRedoService):
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__masinaRepository.read()

    def getMasina(self, idMasina):
        '''
        returnam o masina pe baza unui id dat
        :param idMasina: id de dat
        :return: masina
        '''
        return self.__masinaRepository.read(idMasina)

    def adaugare(self, idMasina, model, anAchizitie, nrKm, inGarantie):
        def help_tool(x): return self.__masinaRepository.adauga(x)
        masina = Masina(idMasina, model, anAchizitie, nrKm, inGarantie)
        self.__masinaValidator.valideaza(masina)
        help_tool(masina)
        self.__undoRedoService.addUndoRedoOperation(
            AddOperation(self.__masinaRepository, masina))

    def stergere(self, idMasina):
        help_tool = lambda x: self.__masinaRepository.sterge(x)
        masina_stearsa = self.__masinaRepository.read(idMasina)
        help_tool(idMasina)

        self.__undoRedoService.addUndoRedoOperation(
            DeleteOperation(self.__masinaRepository, masina_stearsa))

    def modificare(self, idMasina, model, anAchizitie, nrKm, inGarantie):
        masina_veche = self.__masinaRepository.read(idMasina)
        masina = Masina(idMasina, model, anAchizitie, nrKm, inGarantie)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.modifica(masina)
        self.__undoRedoService.addUndoRedoOperation(
            MultiUpdateOperation(self.__masinaRepository,
                                 masina_veche, masina))

    def cautareMasina(self, text):
        '''
        cautam o masina in multimea de masini folosindu-ne de o lista in care
        adaugam un string introdus, iar daca il vom regasi, vom afisa obiectul
        unde a fost regasit
        :param text: textul introdus
        :return: obiectul in care a fost regasit
        '''
        rezultat = self.__masinaRepository.read()
        return list(filter(lambda x: text in x.model or text in x.inGarantie or
                                     text in str(x.nrKm), rezultat))

    def garantieUpdate(self):
        '''
        actualizam garantia daca indeplineste conditiile date
        :return: obiectele cu garantia modificata
        '''
        date = datetime.today()
        year = int(date.strftime("%Y"))

        for masina in self.__masinaRepository.read():
            if int(year - 3) < int(masina.anAchizitie) < (int(year) + 1) and \
                    int(masina.nrKm) < 60001:

                masina.inGarantie = "da"
                masina_veche = self.__masinaRepository.read(masina.idEntitate)
                self.__masinaRepository.modifica(masina)
                self.__undoRedoService.addUndoRedoOperation(
                    MultiUpdateOperation(self.__masinaRepository, masina_veche,
                                         masina))
            else:
                masina.garantie = "nu"
                masina_veche = self.__masinaRepository.read(masina.idEntitate)
                self.__masinaRepository.modifica(masina)
                self.__undoRedoService.addUndoRedoOperation(
                    MultiUpdateOperation(self.__masinaRepository, masina_veche,
                                         masina))

        return self.getAll()

    def generare_random(self, numar, lista, masini, inGarantie, ok, ok2):
        if ok:
            for i in range(0, 10000):
                masini.append("Audi" + str(i))
            inGarantie = ["Da", "Nu"]
            ok = False

        if numar > 0:
            while True:
                idMasina = str(randint(1888, 2021))
                model = choice(masini)
                anAchizitie = randint(1888, 2021)
                nrKm = randint(0, 20000000)
                inGarantie = choice(inGarantie)
                if self.__masinaRepository.read(idMasina) is None:
                    break
            masina = Masina(idMasina, model, anAchizitie, nrKm, inGarantie)
            self.__masinaRepository.adauga(masina)
            lista.append(masina)
            if ok2:
                self.__undoRedoService.addUndoRedoOperation(
                    MultiAdaugareOperation(self.__masinaRepository, lista))
                ok2 = False
            return self.generare_random(numar - 1, lista, masini, inGarantie,
                                        ok, ok2)
        else:
            return None
