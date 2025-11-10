import math


def calc_volume_cubo(s):
    return s**3

def calc_volume_paralelepipedo(l,c,h):
    return l*c*h

def calc_volume_cilindro(r,h):
    return math.pi*r**2*h

def calc_volume_esfera(r):
    return (math.pi*r**3*4)/3

def calc_volume_cone(r, h):
    return (math.pi*r**2*h)/3


forma = input("Insira a forma a ter o volume calculado (Cubo, Paralelepipedo, Cilindro, Esfera ou Cone): ").strip().lower()
if forma == "cubo":
    lado = float(input("Insira o comprimento do lado do cubo: "))
    print(calc_volume_cubo(lado))

elif forma == "paralelepipedo":
    largura = float(input("Insira a largura do paralelepípedo: "))
    comprimento = float(input("Insira o comprimento do paralelepípedo: "))
    altura = float(input("Insira a altura do paralelepípedo: "))
    print(calc_volume_paralelepipedo(largura, comprimento, altura))

elif forma == "cilindro":
    raio = float(input("Insira o raio do cilindro: "))
    altura = float(input("Insira a altura do cilindro: "))
    print(calc_volume_cilindro(raio, altura))

elif forma == "esfera":
    raio = float(input("Insira o raio da esfera: "))
    print(calc_volume_esfera(raio))

elif forma == "cone":
    raio = float(input("Insira o raio do cone: "))
    altura = float(input("Insira a altura do cone: "))
    print(calc_volume_cone(raio, altura))
