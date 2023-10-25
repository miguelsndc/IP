import math


def calculate_distance(x1: int, x2: int, z1: int, z2: int):
    distance_squared = (x1 - x2) ** 2 + (z1 - z2) ** 2
    return math.sqrt(distance_squared)


hogsmeade = (34, 220)
kakariko = (0, 0)
solitude = (140, 456)

x = int(input(""))
z = int(input(""))

print(
    f"Distancia para Hogsmeade: {calculate_distance(x, hogsmeade[0], z, hogsmeade[1]):.2f}"
)
print(
    f"Distancia para Kakariko: {calculate_distance(x, kakariko[0], z, kakariko[1]):.2f}"
)
print(
    f"Distancia para Solitude: {calculate_distance(x, solitude[0], z, solitude[1]):.2f}"
)

