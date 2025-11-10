vmerc = float(input("Valor da mercadoria: "))
vdesc = float(input("Percentual de desconto: "))

print("Valor do desconto: ", vdesc/100 * vmerc)
print("Novo valor da mercadoria: ", (vdesc/100 + 1) * vmerc)