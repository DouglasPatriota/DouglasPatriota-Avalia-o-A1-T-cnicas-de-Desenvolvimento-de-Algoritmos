# TAREFA 9: Média Final (Aritmética ou Ponderada)
PESO_BIMESTRAL = 0.30
PESO_EXAME = 0.40

nota_b1 = float(input("Digite a primeira nota bimestral: "))
nota_b2 = float(input("Digite a segunda nota bimestral: "))
nota_exame = float(input("Digite a nota do exame: "))

media_bimestral = (nota_b1 + nota_b2) / 2

print(f"\nMédia das notas bimestrais: {media_bimestral:.2f}")

if media_bimestral >= 7.0:
    media_final = media_bimestral
    print("Média Bimestral >= 7.0. Média Final = Média Aritmética.")
else:
    media_final = (nota_b1 * PESO_BIMESTRAL) + (nota_b2 * PESO_BIMESTRAL) + (nota_exame * PESO_EXAME)
    print("Média Bimestral < 7.0. Média Final = Média Ponderada.")

print(f"A Média Final do aluno é: {media_final:.2f}")