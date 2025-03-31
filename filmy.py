print("Biblioteka filmów")

import random
import logging
from faker import Faker         
fake = Faker()


logging.basicConfig(level = logging.DEBUG)

#klasa bazowa
class pozycja():
    def __init__(self, tytul, rok, gatunek, liczba_odtworzen = 0):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self):           
        self.liczba_odtworzen += 1

    def __str__(self):
        return f'{self.tytul} {self.rok}'                          
    
    def __repr__(self):
        return f'{self.tytul} {self.rok} - odtworzono: {self.liczba_odtworzen} razy'
    
    
 #klasa film   
class film(pozycja):
    pass


#klasa serial
class serial(pozycja):
    def __init__(self, sezon, odcinek, *args, **kwargs):
        super().__init__(*args, **kwargs)                                
        self.sezon = sezon
        self.odcinek = odcinek

    def __str__(self):
        return f'{self.tytul} {self.rok} S{self.sezon:02}E{self.odcinek:02}'
    
    def __repr__(self):
        return f'{self.tytul} {self.rok} S{self.sezon:02}E{self.odcinek:02} - wyświetlono {self.liczba_odtworzen}'


#funkcja filtruje liste filmów lub seriali
def get_filmy():
    filmy = sorted([f for f in biblioteka if isinstance(f, film)], key = lambda f: f.tytul)
    return filmy

def get_seriale():
    seriale = sorted([s for s in biblioteka if isinstance(s, serial)], key = lambda s: s.tytul)
    return seriale


#funkcja wyszukiwanie pozycji
def search():                                                
    tytul = input(f" \nPodaj tytuł filmu lub serialu:")
    
#wyszukiwarka z możliwością wyboru czy oglądasz i z uruchomieniem funkcji play() - dodaje jedno wyświetlenie po klinięciu t
    for p in biblioteka:
        if tytul in p.tytul:
            print(f'{p.tytul} - {p.liczba_odtworzen} wyświetleń \n')
            ogladasz = input("Chcesz obejrzeć? Wpisz t/n: ")
            if ogladasz == "t":
                p.play()
                print(f'Oglądasz {p.tytul} {p.rok}')
                logging.debug(f'Obejrzano po raz {p.liczba_odtworzen}')
            elif ogladasz == "n":
                return None
            

#generacja wyświetleń
def generate_views(biblioteka, ilosc_powtorzen = 1):
    for i in range (ilosc_powtorzen):
        pozycja = random.choice(biblioteka)
        pozycja.liczba_odtworzen += random.randint(1, 100)
        logging.debug(f"Wyświetlono {pozycja.tytul} {pozycja.liczba_odtworzen} razy")


#top pozycje
def top_pozycje():
    print('\n Top 3 pozycje: \n')
    top_3 = sorted(biblioteka, key = lambda p: p.liczba_odtworzen, reverse = True)[:3]
    for pozycja in top_3:
        print(repr(pozycja))

#testowa biblioteka
#biblioteka = [                      
#    film(tytul = "Pulp Fiction", rok = 1994, gatunek = "Crime"),
#    serial(1, 5,"The Simpsons", 1989, "Comedy"),
#    film("Inception", 2010, "Sci-Fi"),
#    serial(2, 7, "Breaking Bad", 2008, "Drama")
#]


# Lista losowych gatunków
gatunki = ["Comedy", "Drama", "Sci-Fi", "Action", "Crime", "Horror", "Fantasy"]

#generator losowej biblioteki
def generuj_biblioteke(filmy = 5, seriale = 0):
    biblioteka = []

    for _ in range(filmy):                                                                #to do Patryk: mozna zrobić na podstawie słownika, do pobawienia się
        Film = film(
            tytul=fake.sentence(nb_words=3).replace(".", ""),  # Losowy tytuł
            rok=random.randint(1970, 2025),  # Losowy rok
            gatunek=random.choice(gatunki),  # Losowy gatunek
            liczba_odtworzen = random.randint(1, 500)
        )
        biblioteka.append(Film)

    for _ in range(seriale):
        Serial = serial(
            sezon=random.randint(1, 10),
            odcinek=random.randint(1, 20),
            tytul=fake.sentence(nb_words=3).replace(".", ""),
            rok=random.randint(1970, 2025),
            gatunek=random.choice(gatunki),
            liczba_odtworzen = random.randint(1, 500)
        )
        biblioteka.append(Serial)

    return biblioteka



biblioteka = generuj_biblioteke(10, 10)

for element in biblioteka:
    print(element)


#generate_views(biblioteka, 10)

top_pozycje()

search()