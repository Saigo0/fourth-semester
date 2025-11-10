kms = float(input("Quantos km a viagem tem: "))
if kms <= 200:
    viagem = kms * 0.5
    print("Valor da viagem: R$",viagem)
else:
    viagem = kms * 0.45
    print("Valor da viagem: R$",viagem)