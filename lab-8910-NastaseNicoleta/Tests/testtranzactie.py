from Domain.tranzactie import Tranzactie
from Repository.RepositoryInMemory import RepositoryInMemory
from Tests.clearFile import clear_filename


def testTranzactie():

    filename = "lista_tranzactii_text.json"
    clear_filename(filename)
    open(filename, "w").close()

    testam = RepositoryInMemory()

    assert testam.read() == []

    tranzactie = Tranzactie("1", "1", "1", 200, 300, "13/10/2002", "12:23")

    testam.adaugare(tranzactie)

    assert testam.read("1") == tranzactie
