from faker import Faker

fake = Faker('pl_PL')
print(fake.name())

#klasa bazowa
class BaseContact:
    def __init__(self, imie, nazwisko, telefon_prywatny, mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon_prywatny = telefon_prywatny
        self.mail = mail
    def __str__(self):
        return f" {self.imie} \n {self.nazwisko} \n {self.mail} \n"
    
    # funkcja contact() na podstawie oceny instancji
    def contact(self):
        if isinstance(self, BusinessContact):
            telefon = self.telefon_sluzbowy
            return f"Kontaktuję się z {self.imie} {self.nazwisko} na numer sluzbowy: {telefon}"

        elif isinstance(self, BaseContact):
            telefon = self.telefon_prywatny
            return f"Kontaktuję się z {self.imie} {self.nazwisko} na telefon prywatny: {telefon}"
        
    #argument dynamiczny dlugosci kontaktu
    @property
    def dlugosc(self):
        return f"Imie {self.imie}: {len(self.imie)} liter \nNazwisko {self.nazwisko}: {len(self.nazwisko)} liter"

#podklasa od klasy bazowej
class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, telefon_sluzbowy, *args, **kwargs):         #jak args kwargs jest na końcu to dane zaczynaja
        super().__init__(*args, **kwargs)                                              # się od nazwy stanowiska a nie od imienia
        self.stanowisko = stanowisko                                                   # Trzeba wypisywac wsystko z argumentem by ustalic wartosci. 
        self.firma = firma                                                             #Da się inaczej bez określania później wszystkich argumentów nazwanymi?np. firma = , stanowisko =.....
        self.telefon_sluzbowy = telefon_sluzbowy
    
    def __str__(self):
        return f" {self.imie} \n {self.nazwisko} \n {self.mail} \n {self.stanowisko} \n {self.firma} \n telefon sluzbowy:{self.telefon_sluzbowy} \n"


#kreator losowych danych
def generate_data():

    imie = fake.first_name()
    nazwisko = fake.last_name()
    telefon_prywatny = fake.phone_number()
    mail = fake.email()
    stanowisko = fake.job()
    firma = fake.company()
    telefon_sluzbowy = fake.phone_number()

    return imie, nazwisko, telefon_prywatny, mail, stanowisko, firma, telefon_sluzbowy


#kreator listy kontaktów
def create_contacts(base = 5, business = 5):
    kontakty = []

    for k in range(base):
        imie, nazwisko, telefon_prywatny, mail, _, _, _ = generate_data()
        base_contact = BaseContact(imie, nazwisko, telefon_prywatny, mail)
        kontakty.append(base_contact)
    
    for k in range(business):
        imie, nazwisko, telefon_prywatny, mail, stanowisko, firma, telefon_sluzbowy = generate_data()
        businesscontact = BusinessContact(stanowisko, firma, telefon_sluzbowy, imie, nazwisko, telefon_prywatny, mail)
        kontakty.append(businesscontact)

    return kontakty
        

#seweryna = BusinessContact('specjalista','Kenny Rogers', 3839392039, 'Seweryna', 'Rutkowska', 383738293 ,'SewerynaRutkowska@rhyta.com')
#jan = BusinessContact(imie = 'Jan', nazwisko = 'Adamiak', telefon_prywatny = 1242142412, mail = 'konduktoradamiak@onet.pl', firma = 'PKP', stanowisko = 'konduktor', telefon_sluzbowy = 123123123)
#andrzej = BaseContact(imie = 'Andrzej', nazwisko = 'Kalafior', telefon_prywatny = 123123123, mail = 'lubiekalafiory@hot.org')

#wizytowki = [seweryna]
#print(seweryna.contact())
#print(seweryna.dlugosc)



#część wykonawcza
lista_kontaktow = create_contacts(10, 10)

po_imieniu = sorted(lista_kontaktow, key=lambda kontakt: kontakt.imie)

for wiz in po_imieniu:
    print(wiz)

print(po_imieniu[0].contact())
print(po_imieniu[1].contact())
print(po_imieniu[5].contact())
print(po_imieniu[0].dlugosc)