from Domain.masinaValidator import MasinaValidator
from Domain.tranzactieValidator import TranzactieValidator
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.masinaService import MasinaService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService
from Tests.testAll import testAll
from UI.consola import Consola
from Domain.cardClientValidator import CardClientValidator

def main():
    masinaRepositoryJson = RepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    cardRepositoryJson = RepositoryJson("carduri.json")
    cardValidator = CardClientValidator()
    tranzactieRepositoryJson = RepositoryJson("tranzactii.json")
    tranzactieValidator = TranzactieValidator()
    undoRedoService = UndoRedoService()
    masinaService = MasinaService(masinaRepositoryJson, masinaValidator, undoRedoService)
    cardService = CardService(cardRepositoryJson, cardValidator, tranzactieRepositoryJson, undoRedoService)
    tranzactieService = TranzactieService(tranzactieRepositoryJson,
                                          masinaRepositoryJson,
                                          cardRepositoryJson,
                                          masinaService,
                                          cardService,
                                          tranzactieValidator,
                                          undoRedoService)

    consola = Consola(masinaService, cardService, tranzactieService, undoRedoService)

    consola.runMenu()


main()
testAll()