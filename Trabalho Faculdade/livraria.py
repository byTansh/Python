print("Bem vindo a loja do Tiago!")
print("--------------------------------------------\n"
      "---------------MENU PRINCIPAL---------------\n")

lista_livro = []
id_global = 0

def cadastrar_livro():
    global id_global, lista_livro
    id_global += 1
    id = id_global
    print(f"----------------------------------------------\n"
           "-------------MENU CADASTRAR LIVRO-------------\n"
          f"Id do livro: {id}")
    nome = str(input("Digite o nome do livro: ")).lower()
    autor = str(input("Digite o nome do autor: ")).lower()
    editora = str(input("Digite o nome do editora: ")).lower()
    print()

    #dicionario
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    lista_livro.append(livro)

def consultar_livro():
    while True:
        consultarLivroOpcoes = int(input("----------------------------------------------\n"
                                         "-------------MENU CONSULTAR LIVRO-------------\n"
                                         "1 - Consultar Todos os livros: \n"
                                         "2 - Consultar por id de um livro: \n"
                                         "3 - Consultar por autor: \n"
                                         "4 - Retornar ao menu\n"
                                         ">> "))
        print()
        if consultarLivroOpcoes not in [1, 2, 3, 4]:
            print("Opcao invalida")
            continue
        else:
            # Para cada livro na lista de livro ele pega a chave e valor e joga no print
            if consultarLivroOpcoes == 1:
                for livro in lista_livro:
                    for chave, valor in livro.items():
                        print(f"{chave}: {valor}")
                    print()

            # para o livro na lista de livro que tem o id igual ao passado na variavel idLivro, ele busca a chave e o valor
            elif consultarLivroOpcoes == 2:
                idLivro = int(input("Digite o id do livro: "))
                print()
                for livro in lista_livro:
                    if livro['id'] == idLivro:
                        for chave, valor in livro.items():
                            print(f"{chave}: {valor}")
                        print()

            # para o livro na lista de livro que tem o autor igual ao passado na variavel nomeAutor, busca chave e valor
            elif consultarLivroOpcoes == 3:
                nomeAutor = str(input("Digite o nome do autor: ")).lower()
                print()
                for livro in lista_livro:
                    if livro['autor'] == nomeAutor:
                        for chave, valor in livro.items():
                            print(f"{chave}: {valor}")
                        print()
            else:
                break

def remover_livro():
    global lista_livro
    while True:
        opcaoRemover = input("----------------------------------------------\n"
                             "--------------MENU REMOVER LIVRO--------------\n"
                             "Digite o id do livro a ser removido: ")
        if opcaoRemover.strip() != "":
            opcaoRemover = int(opcaoRemover)
            # para cada livro na lista de livro com o id igual ao da opcao remover, ele remove o livro completo
            for livro in lista_livro:
                if livro['id'] == opcaoRemover:
                    lista_livro.remove(livro)
                    print("O livro foi removido com sucesso!\n")
                    break
            else:
                print("O id nao existe, tente outro!\n")
                break
        else:
            print("Insira algum ID valido")
        break

def main():
    while True:
        opcoesDoMenu = int(input("1 - Cadastrar Livro \n"
                                    "2 - Consultar livros \n"
                                    "3 - Remover Livro \n"
                                    "4 - Sair do programa\n"
                                    ">> "))
        print()
        if opcoesDoMenu not in [1, 2, 3, 4]:
            print("opcao invalida, tente novamente")
        else:
            if opcoesDoMenu == 1:
                cadastrar_livro()
            elif opcoesDoMenu == 2:
                consultar_livro()
            elif opcoesDoMenu == 3:
                remover_livro()
            else:
                break

main()