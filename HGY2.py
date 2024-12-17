varosok = ["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]

varos = input("Adj meg egy városnevet: ")

if varos in varosok:  
    i = varosok.index(varos) 
    if i < len(varosok) - 1:
        print(f"A következő város: {varosok[i + 1]}")
    else:
        print("Nincs következő város!")
else:
    varosok.append(varos)
    print(varosok)
