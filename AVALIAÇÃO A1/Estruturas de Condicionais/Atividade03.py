# TAREFA 3: Raízes da Equação do 2º Grau
print("Vamos analisar a equação do 2º grau (ax² + bx + c = 0).")

a = int(input("Digite o coeficiente 'a' (inteiro): "))
b = int(input("Digite o coeficiente 'b' (inteiro): "))
c = int(input("Digite o coeficiente 'c' (inteiro): "))

delta = b ** 2 - 4 * a * c

print(f"\nO Discriminante (Delta) é: {delta}")

if delta < 0:
    print("As raízes da equação são COMPLEXAS (não-reais).")
else:
    print("As raízes da equação são REAIS.")