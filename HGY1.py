mondatok = []
for i in range(5):
    mondat = input(f"Adja meg az {i+1}. mondatot: ")
    mondatok.append(mondat)

 
legtobb_szokoz_mondat = mondatok[0]  
legtobb_szokoz = 0  


for mondat in mondatok:
    szokozok_szama = 0
    for karakter in mondat:
        if karakter == ' ':
            szokozok_szama += 1
    
    
    if szokozok_szama > legtobb_szokoz:
        legtobb_szokoz = szokozok_szama
        legtobb_szokoz_mondat = mondat


print("A legtöbb szóközt tartalmazó mondat:")
print(legtobb_szokoz_mondat)
