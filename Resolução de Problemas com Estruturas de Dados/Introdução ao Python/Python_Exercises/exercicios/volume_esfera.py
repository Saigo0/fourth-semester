import math

def calc_volume_esfera(r):
    return (4*math.pi*r**3)/3

raio = float(input("Digite o raio da esfera: "))
print(calc_volume_esfera(raio))