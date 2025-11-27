# TAREFA 8: Aprovação Simples (Soma das Notas)
LIMITE_APROVACAO = 6.0

nota1 = float(input("Digite a primeira nota bimestral: "))
nota2 = float(input("Digite a segunda nota bimestral: "))

soma_notas = nota1 + nota2

print(f"\nA soma das notas é: {soma_notas:.2f}")

if soma_notas > LIMITE_APROVACAO:
    print("O aluno está APROVADO!")
else:
    print("O aluno está REPROVADO.")