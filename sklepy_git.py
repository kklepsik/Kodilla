sklepy = {'warzywniak': ['kartofle', 'marchew', 'koper'],
          'piekarnia': ['chleb', 'bulki'],
          'kwiaciarnia': ['bukiet roz']
          }

for sklep, produkty in sklepy.items():
    produkty[0] = produkty[0].capitalize()
    print(f'Idę do {sklep.capitalize()} i kupuje: {', '.join(produkty)}')                    #nie ma w gitcie jakiejś funkcji dodaj ostatnie? by za każdym razem nie wpisywać git add 'nazwa pliku'

suma = sum(len(produkty) for produkty in sklepy.values())
print(f"Suma produktów: {suma}")