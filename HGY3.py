import random

veletlen_szamok = [random.randint(-100, 100) for i in range(100)]
print(veletlen_szamok)

positiv_szamok = len([szam for szam in veletlen_szamok if szam > 0])
negativ_szamok = len([szam for szam in veletlen_szamok if szam < 0])


if positiv_szamok > negativ_szamok:
    print("Több 0-nál nagyobb szám van.")
elif negativ_szamok > positiv_szamok:
    print("Több 0-nál kisebb szám van.")

   

