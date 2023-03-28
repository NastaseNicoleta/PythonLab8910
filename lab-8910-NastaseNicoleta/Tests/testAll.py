from Tests.testFunctionalitati import TestFunctionalitati
from Tests.testRepositoryInMemory import test_read_adauga
from Tests.testcard import testCardClient
from Tests.testeService import test_get_all_adauga, test_sterge
from Tests.testmasina import testMasina
from Tests.testtranzactie import testTranzactie


def testAll():
    testMasina()
    testTranzactie()
    testCardClient()
    test_get_all_adauga()
    test_sterge()
    test_read_adauga()
    TestFunctionalitati()
