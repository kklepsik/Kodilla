import logging

logging.basicConfig(level = logging.INFO)
while True:
    operacja = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    print(operacja)
    if operacja.isdigit():
        operacja = int(operacja)
        if operacja in [1, 2, 3, 4]:
            a = input("Podaj pierwszą liczbę: ")
            b = input("Podaj drugą liczbę: ")

            if a.isdigit() and b.isdigit():

                a = float(a)
                b = float(b)

                if operacja == 1:
                    logging.info(f"Dodajesz {a} i {b}")
                    print(f"Wynik to: {int(a) + int(b)}")

                elif operacja == 2:
                    logging.info(f"Odejmujesz {b} od {a}")
                    print(f"Wynik to: {int(a) - int(b)}")

                elif operacja == 3:
                    logging.info(f"Mnożysz {a} i {b}")
                    print(f"Wynik to: {int(a) * int(b)}")

                elif operacja == 4:
                    logging.info(f"Dzielisz {a} przez {b}")
                    print(int(a) / int(b))
                break
            else:
                print("Wpisz liczby! ")
        else:
            print("Wybierz odpowiednią liczbę! ")
    else:
        print("Wybierz liczbę!")
    

