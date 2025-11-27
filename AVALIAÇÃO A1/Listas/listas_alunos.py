alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")

    if nome.lower() == "sair":
        break

    alunos.append(nome)

print("\nAlunos cadastrados:")
for a in alunos:
    print(a)
