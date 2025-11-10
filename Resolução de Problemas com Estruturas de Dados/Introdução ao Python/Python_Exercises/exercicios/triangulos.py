def triangulos (x,y,z):
    if x < y + z or y < x + z or z < x + y:
        if x == y and y == z:
            return "Equilátero"
        elif x == y or y == z or x == z:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é possível formar um triângulo com essas medidas"

for i in range(1,6):
    l1 = float(input(f"Insira o lado 1 do triângulo {i}: "))
    l2 = float(input(f"Insira o lado 2 do triângulo {i}: "))
    l3 = float(input(f"Insira o lado 3 do triângulo {i}: "))
    print(f"Triângulo {i}: ", triangulos(l1,l2,l3))