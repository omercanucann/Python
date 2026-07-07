import math

def get_player_pos():
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip()) # ir string (metin) metodudur. Bir metnin başındaki ve sonundaki boşlukları (ve tab, satır sonu gibi görünmez karakterleri) temizler.
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            return (x, y, z)
        except ValueError:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError as e:
                    print(f"Error on parameter '{part.strip}': {e}")
                    break

print("=== Game Coordinate System ===")

print("Get a first set of coordinates")

pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

distance_center = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2) # Bu ifade, oyuncunun bulunduğu noktanın (0,0,0) merkezine olan uzaklığını hesaplar.

print(f"Distance to center: {round(distance_center, 4)}") # , den sonraki 4 kaç basamak ondalık gösterileceğini belirtir.
print("Get a second set of coordinates")
pos2 = get_player_pos()

distance = math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 + (pos2[2] - pos1[2]) ** 2)

print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")