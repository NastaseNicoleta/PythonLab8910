from Domain.Masina import Masina
from Repository.RepositoryInMemory import RepositoryInMemory
from Tests.clearFile import clear_filename


def testMasina():
    filename = "lista_masini_text.json"
    clear_filename(filename)
    open(filename, "w").close()

    testam = RepositoryInMemory()

    assert testam.read() == []

    masina = Masina("1", "Audi", 2017, 128000, "da")

    testam.adaugare(masina)

    assert testam.read("1") == masina
