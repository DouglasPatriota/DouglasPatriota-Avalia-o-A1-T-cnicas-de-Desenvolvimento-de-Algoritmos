# 🔁 Estruturas de Repetição

Esta pasta contém a solução para a tarefa de criar contadores que exibem apenas números pares no intervalo de 1 a 100, utilizando as estruturas de repetição **`for`** e **`while`**.

## ✔ Critérios de Avaliação Atendidos:
* Implementação correta dos laços (`for` e `while`).
* Uso de operadores lógicos (operador Módulo para verificar paridade).
* Organização do código.

## 📝 Detalhamento dos Contadores

| Arquivo | Estrutura | Lógica de Implementação |
| :--- | :--- | :--- |
| **Contador(FOR).py** | **Laço `for`**. | A iteração é feita com `range(1, 101)`. O uso da condicional `if num % 2 == 0` é fundamental para filtrar e imprimir apenas os números pares. |
| **Contador(While).py** | **Laço `while`**. | A condição `while contador <= 100` controla o loop. Assim como no `for`, a paridade é verificada. É obrigatório o incremento manual da variável `contador` (`contador += 1`) para evitar loops infinitos. |
