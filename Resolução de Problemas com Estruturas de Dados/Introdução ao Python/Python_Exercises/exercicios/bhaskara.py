a1 = float(input('Digite o valor de a: '))
b1 = float(input('Digite o valor de b: '))
c1 = float(input('Digite o valor de c: '))

def bhaskara (a,b,c):
    if a == 0:
        return "Não é uma equação do 2º grau (a=0)."
    delta =  b*b - 4*a*c
    if delta < 0:
        return "Raiz não existente nos números reais"
    x1 = (- b + delta**0.5) / (2 * a)
    x2 = (- b - delta**0.5) / (2 * a)
    return x1, x2

print("Raízes: " + str(bhaskara(a1,b1,c1)))
