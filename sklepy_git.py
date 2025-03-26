sklepy = {'warzywniak': ['kartofle', 'marchew', 'koper'],
          'piekarnia': ['chleb', 'bulki'],
          'kwiaciarnia': ['bukiet roz']
          }

for sklep, produkty in sklepy.items():
    print(f'Idę do {sklep} i kupuje: {', '.join(produkty)}')