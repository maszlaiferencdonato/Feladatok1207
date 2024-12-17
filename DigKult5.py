import random

magassagi_adatok = [random.randint(0, 9) for _ in range(30)]

meredek_ut_elore = 0
for i in range(1, len(magassagi_adatok)):
    if magassagi_adatok[i] >= magassagi_adatok[i-1] + 2:
        meredek_ut_elore += 1

meredek_ut_vissza = 0
for i in range(1, len(magassagi_adatok)):
    if magassagi_adatok[-i] >= magassagi_adatok[-i-1] + 2:
        meredek_ut_vissza += 1

print("Az út magassági adatai:", magassagi_adatok)
print("Meredek szakaszok száma előre:", meredek_ut_elore)
print("Meredek szakaszok száma visszafelé:", meredek_ut_vissza)

