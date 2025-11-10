dias = float(input("Dias: "))
horas = float(input("Horas: "))
minutos = float(input("Minutos: "))
segundos = float(input("Segundos: "))

totsegundos = dias * 3600 * 24 + horas * 3600 + minutos * 60 + segundos

print(totsegundos)