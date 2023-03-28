from Domain.CardClient import CardClient
from Domain.cardClientValidator import CardClientValidator
from Domain.Masina import Masina
from Domain.masinaValidator import MasinaValidator
from Repository.RepositoryInMemory import RepositoryInMemory
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.undoRedoService import UndoRedoService


def test_undo():
    masinaRepository = RepositoryInMemory()
    masinaValidator = MasinaValidator()
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepository,
                                  masinaValidator,
                                  undoRedoService)

    test_masina1 = Masina("1", "Mercedes", 2021, 12000, "da")
    test_masina2 = Masina("2", "Audi", 2012, 130000, "nu")

    masinaService.adaugare("1", "Mercedes", 2021, 12000, "da")
    undoRedoService.undo()

    assert len(masinaRepository.read()) == 0

    masinaService.adaugare("2", "Mercedes", 2021, 12000, "da")
    masinaService.adaugare("3", "Audi", 22012, 130000, "nu")
    undoRedoService.undo()

    assert masinaRepository.read() == [test_masina2]

    undoRedoService.undo()
    assert masinaRepository.read() == []


def test_redo():
    cardClientRepository = RepositoryInMemory()
    cardClientValidator = CardClientValidator()
    tranzactieRepository = RepositoryInMemory()
    undoRedoService = UndoRedoService()
    cardClientService = CardService(cardClientRepository,
                                          cardClientValidator,
                                          tranzactieRepository,
                                          undoRedoService)

    card1 = CardClient("1", "Nastase", "Nicoleta", 2022232135, "12.05.2002",
                 "12.12.2002")
    card2 = CardClient("2", "Popa", "Claudia", 2034543213, "12.05.2002",
                       "12.12.2002")
    card3 = CardClient("3", "Ion", "Daniel", 2023132135, "12.05.2002",
                       "12.12.2002")

    cardClientService.adaugare(
        "1", "Nastase", "Nicoleta", 2022232135, "12.05.2002", "12.12.2002"
    )
    cardClientService.adaugare("2", "Popa", "Claudia", 2034543213, "12.05.2002"
                               , "12.12.2002")
    cardClientService.adaugare("3", "Ion", "Daniel", 2023132135, "12.05.2002",
                               "12.12.2002")

    undoRedoService.undo()
    assert cardClientRepository.read() == [card1, card2]
    undoRedoService.redo()
    assert cardClientRepository.read() == [card1, card2, card3]

    undoRedoService.undo()
    undoRedoService.undo()
    assert cardClientRepository.read() == [card1]
    undoRedoService.redo()
    assert cardClientRepository.read() == [card1, card2]
