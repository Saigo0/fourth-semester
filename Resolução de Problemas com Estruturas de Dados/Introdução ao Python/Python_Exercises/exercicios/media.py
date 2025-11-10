def calc_media(n1,n2,n3, m):
    if m == "A":
        return (n1 + n2 + n3)/3
    if m == "P":
        return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))
tipoM = input("Digite o tipo de média (A ou P): ")

print(calc_media(nota1,nota2,nota3,tipoM))