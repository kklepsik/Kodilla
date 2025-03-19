import logging

logging.basicConfig(level = logging.INFO)

def kalkulator(operacja):
    while True:
        liczby = []
        if operacja == 1:
            while len(liczby) < 10:
                liczba = input("Podaj liczby: ")

                try:
                    liczby.append(float(liczba))
                except:
                    if liczba == "":
                        break
                    else:
                        logging.error("To nie jest liczba!")

            logging.info(f"Dodajesz {liczby}")
            wynik = sum(liczby)

        elif operacja == 2:
            while len(liczby) < 2:
                liczba = input("Podaj liczby: ")

                try:
                    liczby.append(float(liczba))
                except:
                    if liczba == "":
                        break
                    else:
                        logging.error("To nie jest liczba!")

            logging.info(f"Odejmujesz {liczby[1]} od {liczby[0]}")
            wynik = liczby[0] - liczby[1]

        elif operacja == 3:
            while len(liczby) < 10:
                liczba = input("Podaj liczby: ")

                try:
                    liczby.append(float(liczba))
                except:
                    if liczba == "":
                        break
                    else:
                        logging.error("To nie jest liczba!")

            logging.info(f"Mnożysz {liczby}")
            wynik = 1
            for liczba in liczby:
                wynik *= liczba

        elif operacja == 4:
            while len(liczby) < 2:
                liczba = input("Podaj liczby: ")

                try:
                    liczby.append(float(liczba))
                except:
                    if liczba == "":
                        break
                    else:
                        logging.error("To nie jest liczba!")

            if liczby[1] != 0:
                logging.info(f"Dzielisz {liczby[0]} przez {liczby[1]}")
                wynik = liczby[0] / liczby[1]
            else:
                logging.critical(f"Nie dziel przez zero!!!")
                liczby.clear()
                print("Spóbuj jeszcze raz")
                continue

        return f"Oto Twój wynik mordeczko: {wynik}"



while True:
    operacja = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    if int(operacja) in (1, 2, 3, 4):
        operacja = int(operacja) 
        wynik = print(kalkulator(operacja))
        continue      
    else:
        logging.error("Niepoprawna liczba!")

