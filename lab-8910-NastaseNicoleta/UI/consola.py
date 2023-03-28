from datetime import datetime

from Service.masinaService import MasinaService
from Service.cardService import CardService
from Service.tranzactieService import TranzactieService
from Service.undoRedoService import UndoRedoService


class Consola:
    def __init__(self, masinaService: MasinaService, cardService: CardService,
                 tranzactieService: TranzactieService,
                 undoRedoService: UndoRedoService):
        self.__cardService = cardService
        self.__masinaService = masinaService
        self.__tranzactieService = tranzactieService
        self.__undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD masini")
            print("2. CRUD card client")
            print("3. CRUD tranzactie")
            print("4. Cautare masini si clienti")
            print("5. Suma cuprinsa intr-un interval")
            print("6. Ordoneaza masinile descrescator dupa manopera")
            print("7. Ordoneaza carduri descrescator dupa reducere")
            print("8. Stergere tranzactii dintr-un interval de zile")
            print("9. Generare n obiecte")
            print("10. Modificare garantie")
            print("11. Stergere cascada")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDMasiniMenu()
            elif optiune == "2":
                self.runCRUDCardClientMenu()
            elif optiune == "3":
                self.runCRUDTranzactieMenu()
            elif optiune == "4":
                self.uicautareFullText()
            elif optiune == "5":
                self.uiSumaCuprinsaInIntervalSume()
            elif optiune == "6":
                self.uiOrdonareDescrescatorMasiniManopera()
            elif optiune == "7":
                self.uiOrdonareCardClientDescrescator()
            elif optiune == "8":
                self.uiSumaCuprinsaInIntervalSume()
            elif optiune == "9":
                self.uiRandomGenerare()
            elif optiune == "10":
                self.modificareGarantie()
            elif optiune == "11":
                self.uiStergereCascada()
            elif optiune == "u":
                self.__undoRedoService.undo()
            elif optiune == "r":
                self.__undoRedoService.redo()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")

    def runCRUDMasiniMenu(self):
        while True:
            print("1. Adauga masina")
            print("2. Sterge masina")
            print("3. Modifica masina")
            print("a. Afisare")
            print("x. Iesire")

            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaMasina()
            elif optiune == "2":
                self.uiStergeMasina()
            elif optiune == "3":
                self.uiModificaMasina()
            elif optiune == "a":
                self.afiseaza(self.__masinaService.getAll())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")

    def runCRUDCardClientMenu(self):
        while True:
            print("1. Adauga card client:")
            print("2. Sterge card client: ")
            print("3. Modifica (,) card client: ")
            print("a. Afiseaza toate cardurile clientilor: ")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaCardClient()
            elif optiune == "2":
                self.uiStergeCardClient()
            elif optiune == "3":
                self.uiModificareCardClient()
            elif optiune == "a":
                self.afiseaza(self.__cardService.getAllCards())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")

    def runCRUDTranzactieMenu(self):
        while True:
            print("1. Adauga tranzactie")
            print("2. Sterge tranzactie")
            print("3. Modifica tranzactie")
            print("a. Afisare tranzactii")
            print("x. Iesire")

            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaTranzactie()
            elif optiune == "2":
                self.uiStergeTranzactie()
            elif optiune == "3":
                self.uiModificaTranzactie()
            elif optiune == "a":
                self.afiseaza(self.__tranzactieService.getAll())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")

    def uiAdaugaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii: ")
            model = input("Dati modelul masinii: ")
            anAchizitie = int(input("Dati anul achizitiei masinii: "))
            nrKm = int(input("Dati numarul de kilometri al masinii: "))
            inGarantie = input("Dati stadiul garantiei masinii: ")
            self.__masinaService.adaugare(idMasina, model, anAchizitie, nrKm,
                                          inGarantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeMasina(self):
        try:
            idMasina = input("Dati id-ul masinii: ")
            self.__masinaService.stergere(idMasina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de modificat: ")
            model = input("Dati noul model al masinii: ")
            anAchizitie = int(input("Dati noul an al achizitiei masinii: "))
            nrKm = int(input("Dati noul numar de kilometri al masinii: "))
            inGarantie = input("Dati noul stadiu de garantie al masinii: ")
            self.__masinaService.modificare(idMasina, model, anAchizitie, nrKm,
                                            inGarantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def uiAdaugaCardClient(self):
        try:
            idCard = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            data_nasterii = input("Dati data nasterii clientului in format "
                                  "DD/MM/YYY: ")
            data_nasterii = datetime.strptime(data_nasterii, "%d/%m/%Y").date()
            data_inregistrarii = input("Dati data inscrierii clientului"
                                       " in format DD/MM/YYYY: ")
            data_inregistrarii = datetime.strptime(data_inregistrarii,
                                                   "%d/%m/%Y").date()
            self.__cardService.adaugare(idCard, nume, prenume, CNP,
                                        data_nasterii, data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeCardClient(self):
        try:
            idCard = input("Dati id-ul cardului: ")
            self.__cardService.stergere(idCard)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificareCardClient(self):
        try:
            idCard = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            CNP = input("Dati CNP-ul clientului: ")
            data_nasterii = input("Dati data nasterii clientului: ")
            data_nasterii = datetime.strptime(data_nasterii, "%d/%m/%Y").date()
            data_inregistrarii = input("Dati data inscrierii clientului: ")
            data_inregistrarii = datetime.strptime(data_inregistrarii,
                                                   "%d/%m/%Y").date()
            self.__cardService.modificare(idCard, nume, prenume, CNP,
                                          data_nasterii, data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiAdaugaTranzactie(self):
        try:
            idTranzactie = input("Dati id-ul tranzactiei: ")
            idMasina = input("Dati id-ul masinii: ")
            idCardClient = input("Dati id-ul cardului clientului: ")
            sumaPiese = float(input("Dati suma pieselor: "))
            sumaManopera = float(input("Dati suma manoperei: "))
            data = input("Dati data efectuarii tranzactiei: ")
            data = datetime.strptime(data, "%d/%m/%Y").date()
            ora = input("Dati ora efectuarii tranzactiei:")
            ora = datetime.strptime(ora, '%H:%M').time()
            self.__tranzactieService.adaugare(idTranzactie, idMasina,
                                              idCardClient,
                                              sumaPiese,
                                              sumaManopera, data, ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeTranzactie(self):
        try:
            idTranzactie = input("Dati id-ul tranzactiei: ")
            self.__tranzactieService.stergere(idTranzactie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaTranzactie(self):
        try:
            idTranzactie = input("Dati id-ul tranzactiei: ")
            idMasina = input("Dati id-ul masinii: ")
            idCardClient = input("Dati id-ul cardului clientului: ")
            sumaPiese = float(input("Dati suma pieselor: "))
            sumaManopera = float(input("Dati suma manoperei: "))
            data = input("Dati data efectuarii tranzactiei: ")
            data = datetime.strptime(data, "%d/%m/%Y").date()
            ora = input("Dati ora efectuarii tranzactiei:")
            ora = datetime.strptime(ora, "%H:%M").time()
            self.__tranzactieService.modificare(idTranzactie, idMasina,
                                                idCardClient, sumaPiese,
                                                sumaManopera, data, ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uicautareFullText(self):
        text = input("Introduceti textul : ")
        cautare1 = self.__cardService.cautareCardClient(text)
        cautare2 = self.__masinaService.cautareMasina(text)
        print(cautare1)
        print(cautare2)

    def uiSumaCuprinsaInIntervalSume(self):
        try:
            x = int(input("Introduceti limita inferioara : "))
            y = int(input("Introduceti limita superioara : "))
            ok = self.__tranzactieService \
                .afisareTranzactiiCuprinseIntervalSume(x, y)
            print(ok)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiOrdonareDescrescatorMasiniManopera(self):
        try:
            for masini in self.__tranzactieService.ordoneazaMasiniDupaManopera(

            ):
                print(masini)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiOrdonareCardClientDescrescator(self):
        try:
            for card in self.__cardService.ordoneazaCarduriDescrescator():
                print(card)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergereInterval(self):
        try:
            data1 = input("Introdu prima data: ")
            data2 = input("Introdu a doua data: ")
            print(
                self.__tranzactieService.stergereTranzactiiIntervalZile(
                    data1, data2))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiRandomGenerare(self):
        """
        citeste numarul de elemente ce vor fi generate random
        :return: None
        """
        try:
            numar = int(input("Dati numarul masinilor generate automat "))
            self.__masinaService.generare_random(numar, [], [], [], ok=True,
                                                 ok2=True)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def modificareGarantie(self):
        ok = self.__masinaService.garantieUpdate()
        print(ok)

    def uiStergereCascada(self):
        try:
            idSters = input("Introdu id-ul pentru"
                            " a incepe stergerea in cascada: ")
            self.__masinaService.stergere(idSters)
            self.__tranzactieService.stergere(idSters)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
