from Domain.CardClient import CardClient
from Repository.RepositoryInMemory import RepositoryInMemory
from Tests.clearFile import clear_filename


def testCardClient():
    filename = "card_clienti_text.json"
    clear_filename(filename)

    open(filename, "w").close()

    testam = RepositoryInMemory()

    assert testam.read() == []

    card = CardClient("1", "Nastase", "Nicoleta", 202313213, "08/07/2002",
                      "11/10/2020")

    testam.adaugare(card)

    assert testam.read("1") == card
