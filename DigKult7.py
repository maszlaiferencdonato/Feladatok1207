import random


d_magassag = [random.randint(-5, 3) for _ in range(80)]

vizben = 0  
viz_alatt = 0  

for i in d_magassag:
    if i <= 0:
        vizben += 1
        if i < 0:
            viz_alatt += 1

vizben_toltott_ido = vizben / len(d_magassag)
viz_alatt_toltott_ido = viz_alatt / len(d_magassag)

vizben_toltott_ido = vizben * 100
viz_alatt_toltott_ido = viz_alatt * 100

print("A delfin útja:", d_magassag)
print(f"Az út {vizben}% át töltötte a vízben")
print(f"Az út {viz_alatt}% át töltötte a víz alatt")  

