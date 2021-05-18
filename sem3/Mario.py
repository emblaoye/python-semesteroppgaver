class Mario():
    __sekk = {'Fjær'}
    """ En mengde strenger som representerer det Mario har plukket opp"""
    __liv = 3
    """ Livene til Mario """

    def dekrementerLiv(self):
        """ dekrementerer et liv for Mario
        """
        self.__liv -= 1

    def antallLiv(self):
        """ returnerer antall liv Mario har
        """
        return self.__liv

    def erDød(self):
        """ Returner True dersom Mario er død,
        False hvis ikke
        """
        return self.__liv <= 0

    def harVunnet(self):
        """ Returnerer True dersom Mario har
        funnet (og plukket opp) Peach.
        """
        return self.harISekk('Prinsesse Peach')

    def harISekk(self, objektNavn):
        """ Returnerer True dersom Mario har objektNavn
        i sekken
        """
        return objektNavn in self.__sekk

    def plukkOpp(self, objekt):
        """ Tar inn som paramterer et SpillObjekt objekt.
        Dersom det er et liv skal livene inkrementeres med 1.
        Hvis ikke skal objektnavnet (og ikke objektet) puttes i sekken
        Ingenting skjer dersom Mario får et Koopaskall men allerede har et skall fra før.
        """
        if objekt.navn == 'Liv':
            self.__liv += 1
        elif objekt.navn == 'Koopa Troopa':
            if not self.harISekk(objekt.navn):
                self.__sekk.add(objekt.navn)
            else:
                print('Mario kan ikke bære to Koopaskall')
        else:
            self.__sekk.add(objekt.navn)

    def fjernFraSekk(self, objektNavn):
        """ Fjerner objektet ved objektNavn fra sekken
        """
        self.__sekk.remove(objektNavn)

    def printStatus(self):
        """ Printer Mario sine liv og tingene han har
        """
        print(f'Mario har {self.__liv} liv. I sekken har han: {self.__sekk}')