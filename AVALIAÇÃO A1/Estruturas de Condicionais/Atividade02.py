# TAREFA 2: Intervalo em Ordem Crescente
a = float(input("Digite o primeiro limite do intervalo (a): "))
b = float(input("Digite o segundo limite do intervalo (b): "))

if a < b:
    limite_inferior = a
    limite_superior = b
else:
    limite_inferior = b
    limite_superior = a

print(f"O intervalo em ordem crescente é: [{limite_inferior}, {limite_superior}]")
print(f"Representação: {limite_inferior} <= x <= {limite_superior}")