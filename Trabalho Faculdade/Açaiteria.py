
print("Bem-Vindo a Loja do Tiago\n")

# Cardapio de apresentação
print("--------------------Cardápio--------------------\n"
      "------------------------------------------------\n"
      "----| Tamanho | Cupuaçu (CP) |  Açaí (AC)  |----\n"
      "----|    P    |   R$ 9.00    |  R$ 11.00   |----\n"
      "----|    M    |   R$ 14.00   |  R$ 16.00   |----\n"
      "----|    G    |   R$ 14.00   |  R$ 20.00   |----\n"
      "------------------------------------------------\n")

# Variavel valor que irá calcular o valor total
valor = 0.00

# Primeiro laço de repetição, que repetirá o numero de pedidos e caso o usuario erre o Sabor
while True:

    # Validação do sabor 
    Sabor = str(input("Entre com o sabor desejado (CP/AC): ")).upper()
    if Sabor not in ["CP", "AC"]:
        print("Sabor inválido. Tente novamente\n")
        continue
    else:

        # Segundo laço de repetição, que repetirá caso o usuario erre o Tamanho 
        while True:
            
            # Validação do Tamanho
            Tamanho = str(input("Entre com o tamanho desejado (P/M/G): ")).upper()
            if Tamanho not in ["P", "M", "G"]:
                print("Tamanho inválido. Tente novamente\n")
                print(f"entre com o sabor desejado (CP/AC): {Sabor}")
                continue
            else:

                # Validação do preço conforme o Sabor e o Tamanho 
                if Sabor == "CP":
                    if Tamanho == "P":
                        print(f"Você pediu um Cupuaçu tamanho P: R${9.00}\n")
                        valor += 9.00
                    elif Tamanho == "M":
                        print(f"Você pediu um Cupuaçu tamanho P: R${14.00}\n")
                        valor += 14.00
                    else:
                        print(f"Você pediu um Cupuaçu tamanho P: R${18.00}\n")
                        valor += 18.00
                if Sabor == "AC":
                    if Tamanho == "P":
                        print(f"Você pediu um Cupuaçu tamanho P: R${11.00}\n")
                        valor += 11.00
                    elif Tamanho == "M":
                        print(f"Você pediu um Cupuaçu tamanho P: R${16.00}\n")
                        valor += 16.00
                    else:
                        print(f"Você pediu um Cupuaçu tamanho P: R${20.00}\n")
                        valor += 20.00
            # Fim do segundo laço 
            break
        
        # Pedido de repetição de pedido ao cliente 
        pedidos = input("Você deseja realizar outro pedido? (S/N): ").strip().upper()
        print("")
        if pedidos != "S":

            # Soma dos valores dos pedidos 
            print(f"Valor total a ser pago: R${valor}")

            # Fim do ultimo laço 
            break   