from Domain.CardClient import CardClient
from Domain.Masina import Masina
from Domain.tranzactie import Tranzactie
from Repository.RepositoryInMemory import RepositoryInMemory


def test_read_adauga():
    repository_masina = RepositoryInMemory()

    test_masina1 =\
        Masina("1", "Mercedes", 2021, 12000, "da")
    test_masina2 =\
        Masina("2", "Audi", 2012, 130000, "nu")
    repository_masina.adaugare(test_masina1)
    repository_masina.adaugare(test_masina2)

    masini = repository_masina.read()
    assert len(masini) == 2
    assert masini[0] == test_masina1
    assert masini[1] == test_masina2

    assert repository_masina.read("1") == test_masina1
    assert repository_masina.read("2") == test_masina2
    assert repository_masina.read("3") is None

    repository_cardClient = RepositoryInMemory()

    test_card1 =\
        CardClient("1", "Nastase", "Nicoleta", 503123123, "14.03.2002",
                   "12.09.2021")
    test_card2 =\
        CardClient("2", "Cristina", "Ana", 5033213213, "14.05.2002",
                   "12.09.2021")
    repository_cardClient.adaugare(test_card1)
    repository_cardClient.adaugare(test_card2)

    carduri = repository_cardClient.read()
    assert len(carduri) == 2
    assert carduri[0] == test_card1
    assert carduri[1] == test_card2

    assert repository_cardClient.read("1") == test_card1
    assert repository_cardClient.read("2") == test_card2

    repository_tranzactie = RepositoryInMemory()
    test_tranzactie1 = \
        Tranzactie("1", "2", "3", 123, 333, "14.03.2011", "12:20")
    test_tranzactie2 =\
        Tranzactie("2", "3", "4", 1223, 3533, "11.01.2001", "14:20")
    repository_tranzactie.adaugare(test_tranzactie1)
    repository_tranzactie.adaugare(test_tranzactie2)

    tranzactii = repository_tranzactie.read()
    assert len(tranzactii) == 2
    assert tranzactii[0] == test_tranzactie1
    assert tranzactii[1] == test_tranzactie2

    assert repository_tranzactie.read("1") == test_tranzactie1


def test_read_sterge():
    '''
    testam stergerea unui element folosindu-ne de repository
    :return: ...
    '''
    repository_masina = RepositoryInMemory()
    masina1 = Masina("1", "Mercedes", 2021, 12000, "da")
    masina2 = Masina("2", "Audi", 2012, 130000, "nu")
    repository_masina.adaugare(masina1)
    repository_masina.adaugare(masina2)

    masini = repository_masina.read()
    assert len(masini) == 2

    repository_masina.stergere("1")
    masini = repository_masina.read()
    assert len(masini) == 1

    repository_cardClient = RepositoryInMemory()
    cardClient1 =\
        CardClient("1", "Nastase", "Nicoleta", 503123123, "14.03.2002",
                   "12.09.2021")
    cardClient2 =\
        CardClient("2", "Cristina", "Ana", 5033213213, "14.05.2002",
                   "12.09.2021")
    repository_cardClient.adaugare(cardClient1)
    repository_cardClient.adaugare(cardClient2)

    carduri = repository_cardClient.read()
    assert len(carduri) == 2
    repository_cardClient.stergere("1")
    repository_cardClient.stergere("2")
    carduri = repository_cardClient.read()
    assert len(carduri) == 0

    repository_tranzactie = RepositoryInMemory()
    tranzactie1 =\
        Tranzactie("1", "2", "3", 123, 333, "14.03.2011", "12:20")
    tranzactie2 =\
        Tranzactie("2", "3", "4", 1223, 3533, "11.01.2001", "14:20")
    repository_tranzactie.adaugare(tranzactie1)
    repository_tranzactie.adaugare(tranzactie2)

    tranzactii = repository_tranzactie.read()
    assert len(tranzactii) == 2
    repository_tranzactie.stergere("1")
    tranzactii = repository_tranzactie.read()
    assert len(tranzactii) == 1
