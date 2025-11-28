produtos = {}  # Dicionário para armazenar produtos

while True:
    nome = input("Digite o nome do produto (ou 'sair' para finalizar): ")

    if nome.lower() == "sair":
        break

    preco = float(input(f"Digite o preço do produto '{nome}': R$ "))

    produtos[nome] = preco  # Armazena no dicionário

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"Produto: {nome} - Preço: R$ {preco:.2f}")