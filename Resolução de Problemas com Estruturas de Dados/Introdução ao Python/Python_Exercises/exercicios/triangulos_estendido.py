def calc_perimetro_medio(pTot):
    return pTot / 5

def calc_perimetro_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return a + b + c
    else:
        return None

def triangulos(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        perimetro = calc_perimetro_triangulo(x, y, z)
        if x == y and y == z:
            return f"Equilátero, perímetro total: {perimetro}"
        elif x == y or y == z or x == z:
            return f"Isósceles, perímetro total: {perimetro}"
        else:
            return f"Escaleno, perímetro total: {perimetro}"
    else:
        return "Não é possível formar um triângulo com essas medidas"

pTotal = 0
for i in range(1, 6):
    l1 = float(input(f"Insira o lado 1 do triângulo {i}: "))
    l2 = float(input(f"Insira o lado 2 do triângulo {i}: "))
    l3 = float(input(f"Insira o lado 3 do triângulo {i}: "))

    perimetro = calc_perimetro_triangulo(l1, l2, l3)
    if perimetro is not None:
        pTotal += perimetro

    print(f"Triângulo {i}: {triangulos(l1, l2, l3)}")

print("Perímetro médio:", calc_perimetro_medio(pTotal))
