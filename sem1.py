def stigend_eller_synkende(tall1, tall2, tall3):
    print('Tall nr 1:', tall1)
    print('Tall nr 2:', tall2)
    print('Tall nr 3:', tall3)

    if tall1 < tall2 < tall3:
        print('Disse talle er stigende')
    elif tall1 > tall2 > tall3:
        print('Disse tallene er synkende')
    else:
        print('Disse tallene er verken stigende eller synkende')


def kortverdi(kort):
    if kort == 'D':
        verdi = 'Ruter'
    elif kort == 'H':
        verdi = 'Hjerter'
    elif kort == 'S':
        verdi = 'Spar'
    elif kort == 'C':
        verdi = 'Kløver'

    return (verdi)


def tallverdi(tall):
    if tall == 'A':
        verdi = 'Ess'
    elif tall == '2':
        verdi = 'To'
    elif tall == '3':
        verdi = 'Tre'
    elif tall == '4':
        verdi = 'Fire'
    elif tall == '5':
        verdi = 'Fem'
    elif tall == '6':
        verdi = 'Seks'
    elif tall == '7':
        verdi = 'Syv'
    elif tall == '8':
        verdi = 'Åtte'
    elif tall == '9':
        verdi = 'Ni'
    elif tall == '10':
        verdi = 'Ti'
    elif tall == 'J':
        verdi = 'Knekt'
    elif tall == 'Q':
        verdi = 'Dame'
    elif tall == 'K':
        verdi = 'Konge'

    return (verdi)


def korttype():
    verdi = input('Hva er kortverdi?: ')
    tall = input('Hva er tallverdi?: ')

    print('Kortet sin verdi er', kortverdi(verdi), tallverdi(tall))


def tilNok(verdi, kurs):
    if kurs == 'EUR':
        return verdi * 9.68551
    elif kurs == 'USD':
        return verdi * 8.50373
    elif kurs == 'GBP':
        return verdi * 0.92950
    elif kurs == 'AUD':
        return verdi * 6.06501
    elif kurs == 'NOK':
        return verdi


def fraNok(verdi, kurs):
    if kurs == 'EUR':
        return verdi / 9.68551
    elif kurs == 'USD':
        return verdi / 8.50373
    elif kurs == 'GBP':
        return verdi / 0.92950
    elif kurs == 'AUD':
        return verdi / 6.06501
    elif kurs == 'NOK':
        return verdi

def valutakalkulator():
    fraValuta = input('Hvilken valuta ønsker du å konvertere fra?: ')
    tilValuta = input('Hvilken valuta ønsker du å konvertere til?: ')
    verdi = float(input('Hvilken verdi ønsker du å konvertere?: '))

    if fraValuta == 'NOK':
        nyVerdi = fraNok(verdi, tilValuta)
    else:
        nyVerdi = tilNok(verdi, fraValuta)

    print('%f %s er %f %s' % (verdi, fraValuta, nyVerdi, tilValuta))


def oppgave4():
    for i in range(10):
        print('%d**3=%d' %(i, i**3))


def oppgave5():
    start = int(input('Start: '))
    stopp = int(input('Stopp: '))
    n = int(input('Hvilket tall vil du dele på?: '))
    print('Verdier mellom %d og %d som er delelige på %d: ' % (start, stopp, n))
    for i in range(start, stopp+1):
        if i % n == 0:
            print(i)


def tilFahrenheit(celsius):
    return (celsius * 1.8) + 32


def oppgave6a(): #printer en tabell som konverterer fra Celsius til Fahrenheit
    print('%7s %10s %15s' % ('Celsius', 'Farhenheit', 'Status'))
    for i in range(0, 101, 10):
        if i < 60:
            print('%7d %10d Jeg har det bra' % (i, tilFahrenheit(i)))
        else:
            print('%7d %10d Jeg svetter ihjel' % (i, tilFahrenheit(i)))


def renteOkning(verdi, fra, til):
#returnerer hvor mye veriden av pengene har vokst fra året 'fra', til året 'til'
    for i in range(fra, til):
        verdi = verdi*1.02
    return verdi


def oppgave7a():
    print(renteOkning(100, 1910, 2020))

    krone = 19 < renteOkning(1, 1954, 2019)
    if krone:
        print('Krone-is har ikke hatt høyere inflasjon enn 2%')
    else:
        print('Krone-is har hatt høyere inflasjon enn 2%')


def main():
    #korttype()
    #valutakalkulator()
    #oppgave4()
    #oppgave5()
    #oppgave6a()
    #oppgave7a()


main()
