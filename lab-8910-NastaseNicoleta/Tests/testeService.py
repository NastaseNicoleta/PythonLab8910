from Domain.CardClient import CardClient
from Domain.cardClientValidator import CardClientValidator
from Domain.Masina import Masina
from Domain.masinaValidator import MasinaValidator
from Domain.tranzactie import Tranzactie
from Domain.tranzactieValidator import TranzactieValidator
from Repository.RepositoryInMemory import RepositoryInMemory
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService


def test_get_all_adauga():
    repository_masina = RepositoryInMemory()
    validare_masina = MasinaValidator()
    service_masina = MasinaService(repository_masina, validare_masina)

    test_masina1 = Masina("1", "Mercedes", 2021, 12000, "da")
    test_masina2 = Masina("2", "Audi", 2012, 130000, "nu")
    service_masina.adaugare("1", "Mercedes", 2021, 12000, "da")
    service_masina.adaugare("2", "Audi", 2012, 130000, "nu")

    masini = service_masina.getAll()
    assert len(masini) == 2
    assert masini[0] == test_masina1
    assert masini[1] == test_masina2

    repository_cardClient = RepositoryInMemory()
    validare_cardClient = CardClientValidator()
    tranzactieRepository = RepositoryInMemory()
    service_cardClient =\
        CardService(repository_cardClient, validare_cardClient,
                    tranzactieRepository)

    test_card1 =\
        CardClient("1", "Nastase", "Nicoleta", 503123123, "14.03.2002",
                   "12.09.2021")
    test_card2 =\
        CardClient("2", "Cristina", "Ana", 5033213213, "14.05.2002",
                   "12.09.2021")
    service_cardClient\
        .adaugare("1", "Nastase", "Nicoleta", 503123123, "14.03.2002",
                "12.09.2021")
    service_cardClient\
        .adaugare("2", "Cristina", "Ana", 5033213213, "14.05.2002",
                "12.09.2021")

    carduri = service_cardClient.getAll()
    assert len(carduri) == 2
    assert carduri[0] == test_card1
    assert carduri[1] == test_card2

    repository_tranzactie = RepositoryInMemory()
    validare_tranzactie = TranzactieValidator()
    service_tranzactie =\
        TranzactieService(repository_tranzactie,
                          repository_masina,
                          service_masina,
                          service_cardClient,
                          validare_tranzactie)

    test_tranzactie1 = \
        Tranzactie("1", "2", "3", 123, 333, "14.03.2011", "12:20")
    test_tranzactie2 = \
        Tranzactie("2", "3", "4", 1223, 3533, "11.01.2001", "14:20")
    service_tranzactie\
        .adaugare("1", "2", "3", 123, 333, "14.03.2011", "12:20")
    service_tranzactie\
        .adaugare("2", "3", "4", 1223, 3533, "11.01.2001", "14:20")

    tranzactii = service_tranzactie.getAll()
    assert len(tranzactii) == 2
    assert tranzactii[0] == test_tranzactie1
    assert tranzactii[1] == test_tranzactie2


def test_sterge():
    repository_masina = RepositoryInMemory()
    validare_masina = MasinaValidator()
    service_masina = MasinaService(repository_masina, validare_masina)

    service_masina.adaugare("1", "Mercedes", 2021, 12000, "da")
    service_masina.adaugare("2", "Audi", 2012, 130000, "nu")

    masini = service_masina.getAll()
    assert len(masini) == 2

    service_masina.stergere("1")
    masini = service_masina.getAll()
    assert len(masini) == 1

    repository_cardClient = RepositoryInMemory()
    validare_cardClient = CardClientValidator()
    tranzactieRepository = RepositoryInMemory()
    service_cardClient =\
        CardService(repository_cardClient, validare_cardClient,
                    tranzactieRepository)

    service_cardClient\
        .adaugare("1", "Nastase", "Nicoleta", 503123123, "14.03.2002",
                  "12.09.2021")
    service_cardClient\
        .adaugare("2", "Daniela", "As", 5033213213, "14.05.2002", "12.09.2021")

    carduri = service_cardClient.getAllCards()
    assert len(carduri) == 2
    service_cardClient.stergere("1")
    service_cardClient.stergere("2")
    carduri = service_cardClient.getAllCards()
    assert len(carduri) == 0

    repository_tranzactie = RepositoryInMemory()
    validare_tranzactie = TranzactieValidator()
    service_tranzactie =\
        TranzactieService(repository_tranzactie,
                          repository_masina,
                          service_masina,
                          service_cardClient,
                          validare_tranzactie)

    service_tranzactie\
        .adaugare("1", "2", "3", 123, 333, "14.03.2011", "12:20")
    service_tranzactie\
        .adaugare("2", "3", "4", 1223, 3533, "11.01.2001", "14:20")

    tranzactii = service_tranzactie.getAll()
    assert len(tranzactii) == 2
    service_tranzactie.stergere("1")
    tranzactii = service_tranzactie.getAll()
    assert len(tranzactii) == 1


def test_modifica():
    repository_masina = RepositoryInMemory()
    validare_masina = MasinaValidator()
    service_masina = MasinaService(repository_masina, validare_masina)

    test_masina1 = Masina("1", "Mercedes", 2021, 12000, "da")
    test_masina2 = Masina("2", "Audi", 2012, 130000, "nu")
    service_masina.adaugare("1", "Mercedes", 2021, 12000, "da")
    service_masina.adaugare("2", "Audi", 2012, 130000, "nu")

    test_masina3 = Masina("1", "Audi", 2021, 122000, "nu")
    service_masina.modificare("1", "Audi", 2021, 122000, "nu")
