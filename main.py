def badaj_tablice(tablice):
    if len(tablice) == 6 and tablice[0:2].isalpha() and tablice[0:2].isupper() and tablice[2:].isnumeric():
        return (tablice)
    else:
        return False


assert badaj_tablice('') == False
assert badaj_tablice('12') == False
assert badaj_tablice('dw') == False
assert badaj_tablice('d1w234') == False
assert badaj_tablice('DW12345') == False
assert badaj_tablice('DW1234') == 'DW1234'
assert badaj_tablice('AB1CDE') == False


def badaj_auto(znak):
    if znak == 'S':
        return 'osobowy'
    elif znak == 'C':
        return 'ciężarowy'
    else:
        return False


assert badaj_auto('') == False
assert badaj_auto('4') == False
assert badaj_auto('s') == False
assert badaj_auto('S') == 'osobowy'
assert badaj_auto('C') == 'ciężarowy'


def badaj_dystans(dystans):
    if dystans.isdigit():
        return int(dystans)
    else:
        return False


assert badaj_dystans('') == False
assert badaj_dystans('a') == False
assert badaj_dystans('3') == 3
assert badaj_dystans('3g5') == False
assert badaj_dystans('3.5') == False
assert badaj_dystans('¾') == False


# assert badaj_dystans('\u0034') == False

def badaj_godzine(godzina):
    if len(godzina) == 5 and (godzina[1:2] + godzina[3:4]).isnumeric() and godzina[2] == ':':
        return godzina
    else:
        return False


assert badaj_godzine('') == False
assert badaj_godzine('3m3m3') == False
assert badaj_godzine('11:112') == False
assert badaj_godzine('1m:11') == False
assert badaj_godzine('11:11') == '11:11'


def zbadaj_poprawnosc(dane):
    dane = dane.split(sep=' ')
    if len(dane) == 5 and badaj_tablice(dane[0]) and badaj_auto(dane[1]) and badaj_dystans(dane[2]) and badaj_godzine(
            dane[3]) and badaj_godzine(dane[4]):
        return dane
    else:
        return False


assert zbadaj_poprawnosc('DW3123 S 1500 21:00 21:01') == ['DW3123', 'S', '1500', '21:00', '21:01']
assert zbadaj_poprawnosc('DX1234 DROP TABLE USERS S 5500 00:01 00:2') == False
assert zbadaj_poprawnosc('GD3124 C 3500 00:00 00:02') == ['GD3124', 'C', '3500', '00:00', '00:02']
assert zbadaj_poprawnosc('AB1CDE S 1201 12:22 12:23') == False
assert zbadaj_poprawnosc('DW1231 C') == False


def zamien_na_sekundy(godzina):
    return (3600 * int(godzina[0:2]) + 60 * int(godzina[3:5]))


assert zamien_na_sekundy('10:10') == 36600


def czas_przejazdu(poczatek_pomiaru, koniec_pomiaru):
    poczatek_pomiaru = zamien_na_sekundy(poczatek_pomiaru)
    koniec_pomiaru = zamien_na_sekundy(koniec_pomiaru)

    if koniec_pomiaru < poczatek_pomiaru:
        koniec_pomiaru += 86400  # dodana doba w sekundach

    return koniec_pomiaru - poczatek_pomiaru


assert czas_przejazdu('10:10', '10:12') == 120
assert czas_przejazdu('23:59', '00:01') == 120


def licz_predkosc(dystans, czas_przejazdu):
    return int(dystans) / czas_przejazdu * 3600 / 1000


assert licz_predkosc(10, 1) == 36.0


def czy_mandat(predkosc, typ):
    if typ == 'C' and predkosc > 80:
        return 'M'
    elif typ == 'S' and predkosc > 120:
        return 'M'
    else:
        return '.'


def main():
    try:
        while True:
            linia = input("")
            dane = zbadaj_poprawnosc(linia)

            if dane == False:
                print('BLAD')
            else:
                predkosc = licz_predkosc(dane[2], czas_przejazdu(dane[3], dane[4]))
                # speed = f'{predkosc:.2f}'
                print(dane[0], czy_mandat(predkosc, dane[1]), f'{predkosc:.2f}')



    except EOFError:
        pass


if __name__ == '__main__':
    main()
