def calc_tempo_perda(massa):
    tempo = 0
    massaFormat = massa * 1000
    while massaFormat > 0.5:
        massaFormat = massaFormat / 2
        tempo += 50

    return f"Massa inicial: {massa*1000:.2f}g, Massa final: {massaFormat:.2f}g, Tempo: {formata_tempo_perda(tempo)}"

def formata_tempo_perda(tempo):
    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60
    return f"{horas}h {minutos}m {segundos}s"

mass = float(input("Digite a massa do material radioativo (em Kg): "))
print(calc_tempo_perda(mass))
