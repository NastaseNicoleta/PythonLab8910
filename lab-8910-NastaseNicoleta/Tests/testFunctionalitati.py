from datetime import datetime
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Domain.tranzactie import Tranzactie
from Service.undoRedoService import UndoRedoService


class TestFunctionalitati:
    def __init__(self, cardService: CardService, masinaService: MasinaService,
                 tranzactieService: TranzactieService,
                 cardRepository: RepositoryJson,
                 masinaRepository: RepositoryJson,
                 tranzactieRepository: RepositoryJson,
                 undoRedoService: UndoRedoService):
        self.__cardService = cardService
        self.__masinaService = masinaService
        self.__tranzactieService = tranzactieService
        self.__cardRepository = cardRepository
        self.__masinaRepository = masinaRepository
        self.__tranzactieRepository = tranzactieRepository
        self.__undoRedoService = undoRedoService

    #test adaugare random file

    def test_adaugare_cautare(self):
        self.__masinaService.generare_random(3)
        lista = self.__masinaService.getAll()
        assert len(lista) > 0

    #test cautare full text masini

    def test_cautare_full_text(self):
        text = "Audi"
        lista = self.__masinaService.cautareMasina(text)
        assert len(lista) == 3

    # test afisare tranzactii dintr-un interval + ordonari  + stergere
    # tranzactie

    def test_afis_ord_sterg(self):
        self.__masinaService.adaugare("1", "Mercedes", 2021, 12000, "da")
        self.__masinaService.adaugare("2", "Audi", 2012, 130000, "nu")
        self.__cardService.adaugare("1", "Nastase", "Nicoleta", 503123123,
                                    "14.03.2002", "12.09.2021")
        self.__cardService.adaugare("2", "Cristina", "Ana", 5033213213,
                                    "14.05.2002", "12.09.2021")
        t = "tranzactiitest"
        tranzactieRepository = RepositoryJson(t)
        data = datetime.date.today()
        data = data.strftime("%d.%m.%Y")
        data = datetime.datetime.strptime(data, "%d.%m.%Y").date()
        ora = datetime.datetime.now()
        tranzactie = Tranzactie("1", "1", "1", 200, 300, data, ora)
        self.__tranzactieService.adaugare("1", "1", "1", 200, 300, data, ora)
        assert tranzactieRepository.read("1") == tranzactie

        rezultat = self.__tranzactieService.\
            afisareTranzactiiCuprinseIntervalSume(tranzactie.ora,
                                                  tranzactie.ora)
        assert len(rezultat) == 1
        data = datetime.date.today()
        data = data.strftime("%d.%m.%Y")
        data = datetime.datetime.strptime(data, "%d.%m.%Y").date()
        ora = datetime.datetime.now()
        self.__tranzactieService.adaugare("2", "2", "2", data, ora)

        data = datetime.date.today()
        data = data.strftime("%d/%m/%Y")
        data = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        ora = datetime.datetime.now()
        self.__tranzactieService.adaugare("3", "2", "2", data, ora)

        lista = self.__tranzactieService.ordoneazaMasiniDupaManopera()

        i = 2

        for masina in lista:
            assert masina.tranzactie == i
            i -= 1

        lista = self.__cardService.ordoneazaCarduriDescrescator()

        self.__undoRedoService.undo()
        self.__undoRedoService.undo()
        self.__undoRedoService.undo()
        self.__undoRedoService.undo()
        self.__undoRedoService.undo()
        self.__undoRedoService.undo()
        self.__undoRedoService.undo()
        self.__undoRedoService.redo()

        lista = self.__masinaRepository.read()
        assert len(lista) == 1
        self.__undoRedoService.undo()

        lista = self.__cardRepository.read()
        assert len(lista) == 0

        lista = self.__tranzactieRepository.read()
        assert len(lista) == 0

        data = datetime.date.today()
        data = data.strftime("%d/%m/%Y")
        data = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        ora = datetime.datetime.now()
        tranzactie = Tranzactie("1", "1", "1", data, ora)
        self.__tranzactieRepository.adauga(tranzactie)

        # test sterge tranzactii dintr-un anumit interval
        ziua1 = 1
        ziua2 = 31
        self.__tranzactieService.stergereTranzactiiIntervalZile(str(ziua1),
                                                                str(ziua2))
        assert self.__tranzactieRepository.read() == []
        self.__undoRedoService.undo()
        assert self.__tranzactieRepository.read() != []
        self.__undoRedoService.redo()
