# TAREFA 4: Multa de Velocidade
LIMITE_VELOCIDADE = 80
VALOR_MULTA_POR_KM = 5.00

velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > LIMITE_VELOCIDADE:
    excesso_velocidade = velocidade - LIMITE_VELOCIDADE

    valor_multa = excesso_velocidade * VALOR_MULTA_POR_KM

    print("\nVOCÊ FOI MULTADO!")
    print(f"Você excedeu o limite em {excesso_velocidade:.2f} km/h.")
    print(f"O valor da multa é de R$ {valor_multa:.2f}.")
else:
    print("\nVelocidade dentro do limite. Boa viagem!")