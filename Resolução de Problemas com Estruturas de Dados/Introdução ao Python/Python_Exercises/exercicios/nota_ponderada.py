n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

mediaPond = (n1 * 2 + n2 * 3 + n3 * 5) / 10

if mediaPond >= 8:
    conceito = "A"
elif mediaPond >= 7:
    conceito = "B"
elif mediaPond >= 6:
    conceito = "C"
elif mediaPond >= 5:
    conceito = "D"
else:
    conceito = "E"

print(conceito)