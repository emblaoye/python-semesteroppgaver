#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random


def oppgave1():
    """ Printer ut store tall i kort og lang form,
        ofte kalt amerikansk og britisk form.
    """
    store_tall = [
        ["Million", "10^6 ", "10^6 "],
        ["Milliard", "     ", "10^9 "],
        ["Billion", "10^9 ", "10^12"],
        ["Billiard", "     ", "10^15"],
        ["Trillion", "10^12", "10^18"],
        ["Quadrillion", "10^15", "10^24"],
        ["Quintillion", "10^18", "10^30"],
        ["Sextillion", "10^21", "10^36"]
    ]  # Hentet fra https://en.wikipedia.org/wiki/Names_of_large_numbers

    print('%11s %6s %6s' %('Navn', 'Lang', 'Kort'))
    for i in store_tall:
        print('%12s %6s %6s' % (i[0], i[2], i[1]))



def oppgave2():
    """ Henter en rekke tall fra brukeren og ut hva som
        var medianen i listen
    """
    verdier = []  # lager en tom liste
    print('Skriv så mange tall du vil, og avslutt med "ferdig"')

    while True:  # while-løkke som kjører så lenge brukeren skriver inn
        bruker_input = input()
        if bruker_input == 'ferdig':  # hvis brukeren skriver 'ferdig', brytes løkken
            break
        verdier.append(int(bruker_input))  # verdiene legges inn i den tomme listen

    verdier.sort()  # sorterer listen

    # sjekker om antallet i listen er oddetall eller partall
    if len(verdier) % 2:  # listen er oddetall
        median = verdier[int((len(verdier) + 1) / 2) - 1]  # finner medianen
    else:  # listen er partall
        median = (verdier[int(((len(verdier)) / 2) - 1)]
                  + verdier[int((len(verdier)) / 2)]) / 2

    print('Medianen av verdiene er %d' % median)


# I billion USD (kort form)
microsoft_inntekt_dollar = [
    [2002, 28.37],
    [2003, 32.19],
    [2004, 36.84],
    [2005, 39.79],
    [2006, 44.28],
    [2007, 51.12],
    [2008, 60.42],
    [2009, 58.44],
    [2010, 62.48],
    [2011, 69.94],
    [2012, 73.12],
    [2013, 77.85],
    [2014, 86.83],
    [2015, 93.58],
    [2016, 85.32],
    [2017, 89.95],
    [2018, 110.36],
    [2019, 125.84]
]  # Hentet fra https://www.statista.com/statistics/267805/microsofts-global-revenue-since-2002/


def oppgave3a():
    """ Konverterer inntektene fra dollar til kroner
    uten å gjøre endringer på originallisten.
    """
    microsoft_inntekt_kroner = []

    for i in microsoft_inntekt_dollar:
        microsoft_inntekt_kroner.append(i[1] * 8.6862)

    print(microsoft_inntekt_kroner)


def oppgave3b():
    """ Tegner et histogram over inntektene til Microsoft
    """
    year = []
    revenue = []

    for i in microsoft_inntekt_dollar:
        year.append(i[0])
        revenue.append(i[1])

    plt.bar(year, revenue)
    plt.ylabel('In billion USD')
    plt.xlabel('Year')
    plt.show()


def oppgave3c():
    """ Summerer opp inntektene til Microsoft
    """
    sum = 0
    for i in microsoft_inntekt_dollar:
        sum += i[1]

    print('Microsoft tjente %f billioner dollar i perioden 2002-2019' % (sum/1000))



def main():
    """ Dette er filens main-funksjon, det er denne funksjonen som kjører
    når hele filen blir kjørt.
    Hvis du vil kjøre en av oppgave-funksjonene nedenfor fjerner du #-tegnet
    foran oppgave-funksjonen slik at den blir "skrudd på".
    Før du leverer kan det være lurt å sjekke alle funksjonene. Dette gjør
    du ved å fjerne alle #-tegnene nedenfor.
    """
    #oppgave1()
    # print()
    # oppgave2()
    # print()
    # print()
    # oppgave3a()
    # print()
    # oppgave3b()
    # print()
    # oppgave3c()
    # print()


main()



