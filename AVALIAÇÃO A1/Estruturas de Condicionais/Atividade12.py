# TAREFA 12: Altura em relação à média
MEDIA_MASCULINA = 170.7
MEDIA_FEMININA = 158.8

sexo = input("Digite o sexo ('M' para masculino, 'F' para feminino): ").upper().strip()

altura = float(input("Digite a altura em cm (ex: 175.5): "))

if sexo == 'M':
    if altura > MEDIA_MASCULINA:
        print(f"\nAltura ({altura} cm) ACIMA da média masculina ({MEDIA_MASCULINA} cm).")
    else:
        print(f"\nAltura ({altura} cm) ABAIXO ou igual à média masculina ({MEDIA_MASCULINA} cm).")
elif sexo == 'F':
    if altura > MEDIA_FEMININA:
        print(f"\nAltura ({altura} cm) ACIMA da média feminina ({MEDIA_FEMININA} cm).")
    else:
        print(f"\nAltura ({altura} cm) ABAIXO ou igual à média feminina ({MEDIA_FEMININA} cm).")
else:
    print("\nSexo inválido digitado. Por favor, use 'M' ou 'F'.")