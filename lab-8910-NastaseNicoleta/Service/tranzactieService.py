from datetime import date, time

from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.modificareOperation import MultiUpdateOperation
from Domain.multiDeleteOperation import MultiDeleteOperation
from Domain.tranzactie import Tranzactie
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.undoRedoService import UndoRedoService


class TranzactieService:
    def __init__(self, tranzactieRepository: RepositoryJson,
                 masinaRepository: RepositoryJson,
                 cardRepository: RepositoryJson,
                 masinaService: MasinaService,
                 cardService: CardService,
                 tranzactieValidator: TranzactieValidator,
                 undoRedoService: UndoRedoService):
        self.__tranzactieRepository = tranzactieRepository
        self.__tranzactieValidator = tranzactieValidator
        self.__cardRepository = cardRepository
        self.__masinaRepository = masinaRepository
        self.__masinaService = masinaService
        self.__cardService = cardService
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__tranzactieRepository.read()

    def adaugare(self, idTranzactie: str, idMasina: str, idCardClient: str,
                 sumaPiese: float, sumaManopera: float, data: date, ora: time):
        if self.__masinaService.getMasina(idMasina) is not None:
            if self.__masinaService.getMasina(idMasina).inGarantie == "da":
                sumaPiese = 0
        if self.__cardService.GetCard(idCardClient) is not None:
            if self.__cardService.GetCard(idCardClient) is not None:
                sumaManopera = \
                    float(sumaManopera) - (float(sumaManopera) * 0.10)
        tranzactie = Tranzactie(idTranzactie, idMasina, idCardClient,
                                sumaPiese, sumaManopera, data, ora)
        self.__tranzactieValidator.valideaza(tranzactie)
        self.__tranzactieRepository.adauga(tranzactie)
        self.__undoRedoService.addUndoRedoOperation(
            AddOperation(self.__tranzactieRepository, tranzactie))

    def stergere(self, idTranzactie):
        if self.__cardRepository.read(idTranzactie):
            self.__undoRedoService.addUndoRedoOperation(
                DeleteOperation(self.__tranzactieRepository,
                                self.__tranzactieRepository.read(
                                    idTranzactie)))
        self.__tranzactieRepository.sterge(idTranzactie)

    def modificare(self, idTranzactie, idMasina, idCardClient, sumaPiese,
                   sumaManopera, data, ora):
        TranzactieVeche = self.__tranzactieRepository.read(idTranzactie)
        tranzactie = Tranzactie(idTranzactie, idMasina, idCardClient,
                                sumaPiese, sumaManopera, data, ora)

        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista o masina cu acest id! ")

        if self.__cardRepository.read(idCardClient) is None:
            raise KeyError("Nu exista un card cu acest id! ")

        masina = self.__masinaRepository.read(idMasina)

        inGarantie = masina.inGarantie
        if inGarantie != 'da':
            raise KeyError("Nu se poate face tranzactia,"
                           " masina nu mai este in garantie! ")

        self.__tranzactieRepository.modificare(tranzactie)
        self.__undoRedoService.addUndoRedoOperation(
            MultiUpdateOperation(self.__tranzactieRepository, tranzactie,
                                 TranzactieVeche))

    def afisareTranzactiiCuprinseIntervalSume(self, x, y):
        '''
        afisam tranzactiile cuprinse intre doua sume date
        :param x: int
        :param y: int
        :return: suma totala
        '''
        rezultat = []
        for tranzactie in self.getAll():
            sumaTotala = 0
            sumaTotala = tranzactie.sumaPiese + tranzactie.sumaManopera
            if x < sumaTotala < y:
                rezultat.append(tranzactie)
        return rezultat

    def ordoneazaMasiniDupaManopera(self):
        '''
        ordonam dupa reducerile optinute, cardurile clientiilor
        :return: lista ordonata
        '''

        manoperaPerMasini = {}
        rezultat = []
        for masina in self.__masinaRepository.read():
            for tranz in self.__tranzactieRepository.read():
                if tranz.idMasina == masina.idEntitate:
                    manoperaPerMasini[masina.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            manoperaPerMasini[tranzactie.idMasina] \
                .append(tranzactie.sumaManopera)

        for idMasina in manoperaPerMasini:
            rezultat.append(
                {
                    "masina": self.__masinaRepository.read(idMasina),
                    "sumaManopera": manoperaPerMasini[idMasina]
                }
            )
        return sorted(rezultat, key=lambda manopera: manopera["sumaManopera"],
                      reverse=True)

    def stergereTranzactiiIntervalZile(self, ziua1, ziua2):
        '''
        stergerea tuturor tranzactiilor dintr-un anumit interval de zile
        :param ziua1: limita inferioara a intervalului
        :param ziua2: limita superioara a intervalului
        :return:
        '''
        lista = []
        if ziua1 < 1 or ziua1 > 31:
            raise ValueError("Ziua 1 nu e buna ")
        if ziua2 < 1 or ziua2 > 31:
            raise ValueError("Ziua 2 nu e buna ")

        for tranzactie in self.__tranzactieRepository.read():
            if ziua1 <= tranzactie.data.day <= ziua2:
                lista.append(self.__tranzactieRepository.read(tranzactie.
                                                              idEntitate))
                self.stergere(tranzactie.idEntitate)

                self.__undoRedoService.deleteOperation()

        self.__undoRedoService.addUndoRedoOperation(
            MultiDeleteOperation(self.__tranzactieRepository, lista))
