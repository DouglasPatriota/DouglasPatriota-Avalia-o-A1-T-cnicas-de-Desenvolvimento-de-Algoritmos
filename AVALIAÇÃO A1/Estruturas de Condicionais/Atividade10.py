# TAREFA 10: Estacionamento (Lógica central baseada em um exemplo)
TARIFA_INICIAL = 4.00
MINUTOS_INICIAIS = 60
TARIFA_ADICIONAL = 2.00

import math

tempo_minutos = int(input("Digite o tempo total de estacionamento em minutos: "))

if tempo_minutos <= MINUTOS_INICIAIS:

    tarifa_total = TARIFA_INICIAL
else:

    minutos_adicionais = tempo_minutos - MINUTOS_INICIAIS

    horas_adicionais_fração = minutos_adicionais / 60
    horas_cobradas = math.ceil(horas_adicionais_fração)

    tarifa_total = TARIFA_INICIAL + (horas_cobradas * TARIFA_ADICIONAL)

print(f"\nTempo total: {tempo_minutos} minutos")
print(f"A tarifa a ser paga é de R$ {tarifa_total:.2f}")