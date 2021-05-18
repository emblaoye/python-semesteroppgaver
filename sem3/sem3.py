#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SpillObjekt import SpillObjekt
from Mario import Mario
from random import random
import re

brettSymbol = {
    'S': SpillObjekt('Super Mario', '🔴', 'Spiller'),
    # For at Mario skal kunne "ta med" Peach
    'P': SpillObjekt('Prinsesse Peach', '💍', 'Kan plukkes'),
    'B': SpillObjekt('Bowser', '👺', 'Fiende'),
    'G': SpillObjekt('Goomba', '💩', 'Fiende'),
    'K': SpillObjekt('Koopa Troopa', '🐢', 'Fiende'),
    'C': SpillObjekt('Cap', '🧢', 'Kan plukkes'),
    'L': SpillObjekt('Liv', '🍄', 'Kan plukkes'),
    'V': SpillObjekt('Vegg', '⬜', 'Vegg'),
    'Y': SpillObjekt('Yttervegg', '⬜', 'Vegg'),
    '.': SpillObjekt('Ingenting', '.', 'Luft')
}

fiender = {
    'Bowser': (0.5, 3),
    'Goomba': (0.8, 1),
    'Koopa Troopa': (0.7, 1)
}


def lesInnBrettFraFil(brettFil):
    """ Parameteret brettFil er navnet på filen som leses.
    Brettet leses inn til en 2-dimensjonal liste, der den
    ytre listen inneholder radene, mens de indre listene
    inneholder kolonnene for den raden de representerer.
    """
    board = []

    with open(brettFil) as fil:
        for line in fil:
            board.append(list(line.rstrip('\n')))

    return board


def finnMario(brett):
    """ Returnerer posisjonen til Mario i den todimensjonale
    listen brett.
    Husk at (0, 0) er oppe til venstre.
    """
    MarioPos = (0, 0)

    for idxRow, row in enumerate(brett):
        for idxCol, col in enumerate(row):
            if col == 'S':
                MarioPos = (idxRow, idxCol)

    return MarioPos


def printBrett(brett):
    """ Tar inn som parameter en todimensjonal liste brett,
    og printer brett til konsollen
    """
    for row in brett:
        lineString = ''
        for char in row:
            lineString += "{:2}".format(brettSymbol[char].vis)
        print(lineString)


def flyttMario(brett, gammelPos, nyPos):
    """ Flytter Mario fra den gamle posisjonen til den
    nye posisjonen. Den gamle posisjonen vil inneholde luft.
    Funksjonen gjør endringer på brettet, men returnerer ingenting.
    """
    brett[nyPos[0]][nyPos[1]] = 'S'
    brett[gammelPos[0]][gammelPos[1]] = '.'


def kjemp(mario, fiende):
    """ Lar Mario kjempe mot en fiende.
    Informasjon om fienden kan slås opp i oppslagstabellen fiender.
    Her finner du sjansen for å lykkes ved å hoppe på fienden, og
    antall liv fienden starter med.
    Mario kan enten hoppe på fienden, med risiko for å bomme og
    miste et liv, eller kaste et Koopaskall på fienden dersom
    Mario har dette i sekken.
    Koopaskall vil alltid ta et liv av fienden.
    Dersom Mario vinner over Koopa Troopa, får han et Koopaskall.
    Dersom Mario møter Bowser uten capen sin, mister han automatisk
    to liv.
    """
    print(f'Super Mario har truffet på {fiende.navn}')

    fiendeLiv = fiender.get(fiende.navn)[1]
    fiendeChance = fiender.get(fiende.navn)[0]

    if fiende.navn == 'Bowser' and not mario.harISekk('Cap'):
        print('Super Mario mister 2 liv for å møte Bowser uten Cap!')
        mario.dekrementerLiv()
        mario.dekrementerLiv()

    while fiendeLiv > 0 and not mario.erDød():
        print(f'Mario har {mario.antallLiv()} liv, {fiende.navn} har {fiendeLiv} liv')
        choice = input('Velg h for å hoppe på fienden, k for å kaste skall')
        while choice != 'h' and choice != 'k':
            print('Ugyldig valg!')
            choice = input('Velg h for å hoppe på fienden, k for å kaste skall')
        if choice == 'k':
            if not mario.harISekk('Koopa Troopa'):
                print('Mario har ikke noe skall i sekken!')
            else:
                print(f'Mario kaster skallet sitt og tar ett liv av {fiende.navn}')
                fiendeLiv -= 1
                mario.fjernFraSekk('Koopa Troopa')
        else:
            if random() < fiendeChance:
                print(f'Mario tok ett liv av {fiende.navn}')
                fiendeLiv -= 1
                if fiende.navn == 'Koopa Troopa' and fiendeLiv <= 0:
                    mario.plukkOpp(brettSymbol.get('K'))
            else:
                print('Mario bommet på hoppet sitt og mistet ett liv')
                mario.dekrementerLiv()
    if mario.erDød():
        print('Mario er død')
    else:
        print(fiende.navn, 'er død')


def interagerMedObjekt(mario, objekt):
    """ Lar Mario interagere med objektet som befinner seg der Mario vil gå.
    Dersom objektet er av kategorien 'Kan plukkes', så skal Mario plukke opp
    objektet. Dersom objektet er av kategorien 'Fiende' så skal Mario kjempe
    mot fienden.
    """
    if objekt.kategori == 'Kan plukkes':
        mario.plukkOpp(objekt)
    elif objekt.kategori == 'Fiende':
        kjemp(mario, objekt)
    elif objekt.kategori == 'Luft':
        pass  # Denne sjekken er ikke nødvendig, men kan øke kodens leseligheten


def hentRetning(gammelPos):
    """ Spør brukeren etter en retning, og kalkulerer den nye retningen
    basert på brukerens input. Gjentas helt til retningen er gyldig
    """
    newDirection = input('Oppgi en retning: w (opp), d (hoyre), s (ned) eller a (venstre)')
    pattern = re.compile('[asdw]')

    while not pattern.match(newDirection):
        print('Ikke gyldig retning')
        newDirection = input('Oppgi en retning: w (opp), d (hoyre), s (ned) eller a (venstre)')

    if newDirection == 'w':
        return (gammelPos[0] - 1, gammelPos[1])
    elif newDirection == 'd':
        return (gammelPos[0], gammelPos[1] + 1)
    elif newDirection == 'a':
        return (gammelPos[0], gammelPos[1] - 1)
    else:
        return (gammelPos[0] + 1, gammelPos[1])


def gå(brett, mario, marioPos):
    """ Spør brukeren etter en retning, går et steg i retningen
    og returnerer en tuppel av heltall med mario sin nye
    posisjon på brettet. Funskjonen sørger også for at brettet
    er oppdatert.
    Dersom retningen ikke er gyldig må brukeren gi en ny retning
    helt til retningen er gyldig.
    Dersom retningen er gyldig må Mario interagere med objektet
    i den nye posisjonen
    """
    goTo = hentRetning(marioPos)
    squareObject = brettSymbol.get(brett[goTo[0]][goTo[1]])

    while squareObject.kategori == 'Vegg':
        print('Det er en vegg her, gå en annen retning')
        goTo = hentRetning(marioPos)
        squareObject = brettSymbol.get(brett[goTo[0]][goTo[1]])

    interagerMedObjekt(mario, squareObject)
    flyttMario(brett, marioPos, goTo)

    return goTo


def spillLøkke(brett, mario, marioPos):
    """ Starter løkken som kjører spillet med den todimensjonale
    listen brett og mario. Løkken avsluttes når spillet er over.
    """
    while True:
        printBrett(brett)
        print()
        mario.printStatus()
        marioPos = gå(brett, mario, marioPos)
        if mario.erDød():
            print('Game over.')
            break
        if mario.harVunnet():
            print('Mario vant!')
            break


def main():
    """ Leser inn brettet fra fil og starter spillet
    """
    brett = lesInnBrettFraFil('level1.txt')
    mario = Mario()
    marioPos = finnMario(brett)
    spillLøkke(brett, mario, marioPos)


main()
