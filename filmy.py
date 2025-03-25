print("Biblioteka filmów")

import random
#from faker import Faker            #instalowałem ale nie działa, chcialbym dodac funkcje ktora uzupelnia biblioteke

class pozycja():
    def __init__(self, tytul, rok, gatunek, liczba_odtworzen = 0):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self): 
        self.liczba_odtworzen += 1

    def __str__(self):
        return f'{self.tytul} {self.rok}'                              #nie rozumiem róznicy między str i repr
    
    def __repr__(self):
        return f'{self.tytul} {self.rok} - odtworzono: {self.liczba_odtworzen} razy'
    
    
class film(pozycja):
    pass


class serial(pozycja):
    def __init__(self, sezon, odcinek, *args, **kwargs):
        super().__init__(*args, **kwargs)                                 #args i kwargs zaburzją kolejność argumentów, z tego względu wydaje sie łatwiej wypisac wszystkie argumenty od nowa
        self.sezon = sezon
        self.odcinek = odcinek



    def __str__(self):
        return f'{self.tytul} {self.rok} S{self.sezon:02}E{self.odcinek:02}'
    
    def __repr__(self):
        return f'{self.tytul} {self.rok} S{self.sezon:02}E{self.odcinek:02} - wyświetlono {self.liczba_odtworzen}'

def get_filmy():
    filmy = sorted([f for f in biblioteka if isinstance(f, film)], key = lambda f: f.tytul)
    return filmy

def get_seriale():
    seriale = sorted([s for s in biblioteka if isinstance(s, serial)], key = lambda s: s.tytul)
    return seriale

#def search():
#    tytul = input("Podaj tytuł filmu lub serialu:")
#    return [p for p in biblioteka if tytul in p.tytul]                      # a co jak tutaj chciałbym jeszcze dodać liczbę wyświetleń? i dalej funkcje czy chcesz obejrzec?

def generate_views(biblioteka, ilosc_powtorzen = 1):
    for i in range (ilosc_powtorzen):
        pozycja = random.choice(biblioteka)
        pozycja.liczba_odtworzen += random.randint(1, 100)
        print(f"Wyświetlono {pozycja.tytul} {pozycja.liczba_odtworzen} razy")

def top_pozycje():
    print('\n Top 3 pozycje: \n')
    top_3 = sorted(biblioteka, key = lambda p: p.liczba_odtworzen, reverse = True)[:3]
    for pozycja in top_3:
        print(repr(pozycja))

biblioteka = [                                                            #trzeba wymienaic wszystkie zmienne przy zaburzeniu kolejnosci przez args i kwargs
    film(tytul = "Pulp Fiction", rok = 1994, gatunek = "Crime"),
    serial(1, 5,"The Simpsons", 1989, "Comedy"),
    film("Inception", 2010, "Sci-Fi"),
    serial(2, 7, "Breaking Bad", 2008, "Drama")
]

for element in biblioteka:
    print(element)

for film in get_filmy():
    print(film)

#for pozycja in search():
 #   print(pozycja)

generate_views(biblioteka, 10)

top_pozycje()

