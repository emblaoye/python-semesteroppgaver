#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SpillObjekt import SpillObjekt
from Mario import Mario
from random import random
import re

brettSymbol = {
    'S': SpillObjekt('Super Mario', '๐ด', 'Spiller'),
    # For at Mario skal kunne "ta med" Peach
    'P': SpillObjekt('Prinsesse Peach', '๐', 'Kan plukkes'),
    'B': SpillObjekt('Bowser', '๐บ', 'Fiende'),
    'G': SpillObjekt('Goomba', '๐ฉ', 'Fiende'),
    'K': SpillObjekt('Koopa Troopa', '๐ข', 'Fiende'),
    'C': SpillObjekt('Cap', '๐งข', 'Kan plukkes'),
    'L': SpillObjekt('Liv', '๐', 'Kan plukkes'),
    'V': SpillObjekt('Vegg', 'โฌ', 'Vegg'),
    'Y': SpillObjekt('Yttervegg', 'โฌ', 'Vegg'),
    '.': SpillObjekt('Ingenting', '.', 'Luft')
}

fiender = {
    'Bowser': (0.5, 3),
    'Goomba': (0.8, 1),
    'Koopa Troopa': (0.7, 1)
}


def lesInnBrettFraFil(brettFil):
    """ Parameteret brettFil er navnet pรฅ filen som leses.
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
    Funksjonen gjรธr endringer pรฅ brettet, men returnerer ingenting.
    """
    brett[nyPos[0]][nyPos[1]] = 'S'
    brett[gammelPos[0]][gammelPos[1]] = '.'


def kjemp(mario, fiende):
    """ Lar Mario kjempe mot en fiende.
    Informasjon om fienden kan slรฅs opp i oppslagstabellen fiender.
    Her finner du sjansen for รฅ lykkes ved รฅ hoppe pรฅ fienden, og
    antall liv fienden starter med.
    Mario kan enten hoppe pรฅ fienden, med risiko for รฅ bomme og
    miste et liv, eller kaste et Koopaskall pรฅ fienden dersom
    Mario har dette i sekken.
    Koopaskall vil alltid ta et liv av fienden.
    Dersom Mario vinner over Koopa Troopa, fรฅr han et Koopaskall.
    Dersom Mario mรธter Bowser uten capen sin, mister han automatisk
    to liv.
    """
    print(f'Super Mario har truffet pรฅ {fiende.navn}')

    fiendeLiv = fiender.get(fiende.navn)[1]
    fiendeChance = fiender.get(fiende.navn)[0]

    if fiende.navn == 'Bowser' and not mario.harISekk('Cap'):
        print('Super Mario mister 2 liv for รฅ mรธte Bowser uten Cap!')
        mario.dekrementerLiv()
        mario.dekrementerLiv()

    while fiendeLiv > 0 and not mario.erDรธd():
        print(f'Mario har {mario.antallLiv()} liv, {fiende.navn} har {fiendeLiv} liv')
        choice = input('Velg h for รฅ hoppe pรฅ fienden, k for รฅ kaste skall')
        while choice != 'h' and choice != 'k':
            print('Ugyldig valg!')
            choice = input('Velg h for รฅ hoppe pรฅ fienden, k for รฅ kaste skall')
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
                print('Mario bommet pรฅ hoppet sitt og mistet ett liv')
                mario.dekrementerLiv()
    if mario.erDรธd():
        print('Mario er dรธd')
    else:
        print(fiende.navn, 'er dรธd')


def interagerMedObjekt(mario, objekt):
    """ Lar Mario interagere med objektet som befinner seg der Mario vil gรฅ.
    Dersom objektet er av kategorien 'Kan plukkes', sรฅ skal Mario plukke opp
    objektet. Dersom objektet er av kategorien 'Fiende' sรฅ skal Mario kjempe
    mot fienden.
    """
    if objekt.kategori == 'Kan plukkes':
        mario.plukkOpp(objekt)
    elif objekt.kategori == 'Fiende':
        kjemp(mario, objekt)
    elif objekt.kategori == 'Luft':
        pass  # Denne sjekken er ikke nรธdvendig, men kan รธke kodens leseligheten


def hentRetning(gammelPos):
    """ Spรธr brukeren etter en retning, og kalkulerer den nye retningen
    basert pรฅ brukerens input. Gjentas helt til retningen er gyldig
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


def gรฅ(brett, mario, marioPos):
    """ Spรธr brukeren etter en retning, gรฅr et steg i retningen
    og returnerer en tuppel av heltall med mario sin nye
    posisjon pรฅ brettet. Funskjonen sรธrger ogsรฅ for at brettet
    er oppdatert.
    Dersom retningen ikke er gyldig mรฅ brukeren gi en ny retning
    helt til retningen er gyldig.
    Dersom retningen er gyldig mรฅ Mario interagere med objektet
    i den nye posisjonen
    """
    goTo = hentRetning(marioPos)
    squareObject = brettSymbol.get(brett[goTo[0]][goTo[1]])

    while squareObject.kategori == 'Vegg':
        print('Det er en vegg her, gรฅ en annen retning')
        goTo = hentRetning(marioPos)
        squareObject = brettSymbol.get(brett[goTo[0]][goTo[1]])

    interagerMedObjekt(mario, squareObject)
    flyttMario(brett, marioPos, goTo)

    return goTo


def spillLรธkke(brett, mario, marioPos):
    """ Starter lรธkken som kjรธrer spillet med den todimensjonale
    listen brett og mario. Lรธkken avsluttes nรฅr spillet er over.
    """
    while True:
        printBrett(brett)
        print()
        mario.printStatus()
        marioPos = gรฅ(brett, mario, marioPos)
        if mario.erDรธd():
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
    spillLรธkke(brett, mario, marioPos)


main()
