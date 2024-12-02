LIMITE_CRITICO = 5
estoque = []


def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip().replace(" ", "_")
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            break
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")

    produto = {"nome": nome, "quantidade": quantidade}
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")


def verificar_estado_critico():
    print(f"\nProdutos em estado crítico (quantidade abaixo de {LIMITE_CRITICO}):")
    encontrou = False
    for produto in estoque:
        if produto["quantidade"] < LIMITE_CRITICO:
            print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}")
            encontrou = True
    if not encontrou:
        print("Nenhum produto em estado crítico.")


def gerar_relatorio():
    print("\nRelatório do Estoque:")
    print("---------------------")
    for produto in estoque:
        status = " (CRÍTICO)" if produto["quantidade"] < LIMITE_CRITICO else ""
        print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}{status}")


def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Exibir Produtos em Estado Crítico")
        print("3. Gerar Relatório do Estoque")
        print("4. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            verificar_estado_critico()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")


if __name__ == "__main__":
    menu()
