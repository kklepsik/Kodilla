print("Palindromy")

"""porownanie slowa z odwroconym stringiem tego slowa
nastepnie wydrukuj czy jest lub nie jest palindromem"""

def palindrom(slowo):
    if slowo == slowo[::-1]:
        return print(True)
    else:
        return print(False)
    
palindrom("potop")