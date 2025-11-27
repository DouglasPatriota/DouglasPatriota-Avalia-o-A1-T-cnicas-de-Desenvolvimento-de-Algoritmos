# TAREFA 11: Cálculo de Preço de Viagem

distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco_total = distancia * 0.50
    tarifa = 0.50
elif distancia <= 400:
    preco_total = distancia * 0.45
    tarifa = 0.45
else:
    preco_total = distancia * 0.40
    tarifa = 0.40

print("-" * 30)
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Tarifa aplicada: R$ {tarifa:.2f} por km")
print(f"O preço total da viagem é: R$ {preco_total:.2f}")
print("-" * 30)