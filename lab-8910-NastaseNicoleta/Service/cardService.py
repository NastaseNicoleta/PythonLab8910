from datetime import date
from functools import reduce

from Domain.CardClient import CardClient
from Domain.addOperation import AddOperation
from Domain.cardClientValidator import CardClientValidator
from Domain.deleteOperation import DeleteOperation
from Domain.modificareOperation import MultiUpdateOperation
from Repository.repositoryJson import RepositoryJson
from Service.undoRedoService import UndoRedoService


class CardService:
    def __init__(self, cardRepository: RepositoryJson,
                 cardClientValidator: CardClientValidator,
                 tranzactieRepository: RepositoryJson,
                 undoRedoService: UndoRedoService):
        self.__cardRepository = cardRepository
        self.__cardClientValidator = cardClientValidator
        self.__tranzactieRepository = tranzactieRepository
        self.__undoRedoService = undoRedoService

    def getAllCards(self):
        return self.__cardRepository.read()

    def adaugare(self, idCard: str, nume: str, prenume: str, CNP: str,
                 data_nasterii: date,
                 data_inregistrarii: date):
        for card in self.__cardRepository.read():
            if CNP == card.CNP:
                raise KeyError("CNP-ul exista deja! ")
        card = CardClient(idCard, nume, prenume, CNP, data_nasterii,
                          data_inregistrarii)
        self.__cardClientValidator.valideaza(card)
        self.__cardRepository.adauga(card)
        self.__undoRedoService.addUndoRedoOperation(AddOperation(
            self.__cardRepository, card
        ))

    def stergere(self, idCard):
        card_sters = self.__cardRepository.read(idCard)
        self.__cardRepository.sterge(idCard)
        self.__undoRedoService.addUndoRedoOperation(
            DeleteOperation(self.__cardRepository, card_sters))

    def modificare(self, idCard, nume, prenume, CNP, data_nasterii,
                   data_inregistrarii):
        card_vechi = self.__cardRepository.read(idCard)
        for card in self.__cardRepository.read():
            if CNP == card.cnp:
                raise KeyError("CNP-ul exista deja! ")
        card = CardClient(idCard, nume, prenume, CNP, data_nasterii,
                          data_inregistrarii)
        self.__cardClientValidator.valideaza(card)
        self.__cardRepository.modifica(card)
        self.__undoRedoService.addUndoRedoOperation(
            MultiUpdateOperation(self.__cardRepository, card_vechi, card))

    def GetCard(self, idCardClient):
        '''

        :param idCardClient: id ul card-ului
        :return: un card pe baza id-ului dat in caz ca acesta exita
        '''
        return self.__cardRepository.read(idCardClient)

    def cautareCardClient(self, text):
        '''
        cautam un card  in multimea de carduri folosindu-ne de o lista in care
        adaugam un string introdus, iar daca il vom regasi, vom afisa obiectul
        unde a fost regasit
        :param text: textul introdus
        :return: obiectul in care a fost regasit
        '''
        rezultat = self.__cardRepository.read()
        return list(filter(lambda x: text in x.nume or text in x.prenume or
                                     text in x.CNP or text in
                                     str(x.data_nasterii) or text in
                                     str(x.data_inregistrarii), rezultat))

    def ordoneazaCarduriDescrescator(self):
        '''
        ordoneaza descrescator dupa suma optinuta pe manopera ,
        folosind un dictionar
        :return: o lista sortata
        '''
        reducerePerCard = {}
        rezultat = []
        for card in self.__cardRepository.read():
            for tranz in self.__tranzactieRepository.read():
                if tranz.idCardClient == card.idEntitate:
                    reducerePerCard[card.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            reducerePerCard[tranzactie.idCardClient] \
                .append(tranzactie.sumaManopera)

        for idCardClient in reducerePerCard:
            reduceri = reducerePerCard[idCardClient]
            rezultat.append(
                {
                    "card": self.__cardRepository.read(idCardClient),
                    "valoare": reduce(lambda x, y: x + y, reduceri)
                }
            )

        return sorted(rezultat, key=lambda reducere: reducere["valoare"],
                      reverse=True)

    @staticmethod
    def sortedddd(lista, key, reverse: bool):
        if reverse:
            for i in range(0, len(lista) - 1):
                for j in range(i + 1, len(lista)):
                    if key(lista[i]) < key(lista[j]):
                        lista[i], lista[j] = lista[j], lista[i]
        else:
            for i in range(1, len(lista) - 2):
                for j in range(i + 1, len(lista) - 1):
                    if key(lista[i] > lista[j]):
                        lista[i], lista[j] = lista[j], lista[i]
        return lista
