kWh = float(input("KWh: "))
tipo = input("Tipo de instalação: ")

if tipo == "R":
    if kWh > 500:
        preco = kWh * 0.65
        print("Valor R$ %.2f" % preco)
    else:
        preco = kWh * 0.4
        print("Valor R$ %.2f" % preco)

if tipo == "C":
    if kWh > 1000:
        preco = kWh * 0.60
        print("Valor R$ %.2f" % preco)
    else:
        preco = kWh * 0.55
        print("Valor R$ %.2f" % preco)

if tipo == "I":
    if kWh > 5000:
        preco = kWh * 0.68
        print("Valor R$ %.2f" % preco)
    else:
        preco = kWh * 0.57
        print("Valor R$ %.2f" % preco)

