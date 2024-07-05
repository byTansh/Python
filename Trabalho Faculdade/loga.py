#Comando que irá imprimiar a mensagem de boas-vindas junto com meu nome [exigência de codigo 1 de 6]#
print("Bem-vindo a loja do Tiago")

#Input para declarar valor e quantidade [exigência de codigo 2 de 6]#
valorUnitario = float(input("Entre com o valor do produto: "))
qtd = int(input("Entre com a quantidade do produto: "))

valorTotal = valorUnitario * qtd
Desconto = valorTotal / 100

#Uso do if/efli/else para estrutura condicional [exigência de codigo 3 de 6]#
if (valorTotal < 2500):
    print(f"O valor total SEM o desconto é: R${valorTotal:.2f}")
    print(f"O valor total COM o desconto é: R${valorTotal:.2f}")

elif (valorTotal >= 2500 and valorTotal < 6000):

    #Saida com ValorTotal da compra [exigência de codigo 4 de 6]#
    print(f"O valor total SEM o desconto é: R${valorTotal:.2f}")

    #Input para declarar valor e quantidade [exigência de codigo 3 de 6]#
    #Saida com ValorTotal da compra + desconto [exigência de codigo 4 de 6]#
    print(f"O valor total COM desconto é: R${valorTotal - (4 * Desconto):.2f}")

elif (valorTotal >= 6000 and valorTotal < 10000):
    print(f"O valor total SEM o desconto é: R${valorTotal:.2f}")
    print(f"O valor total COM desconto é: R${valorTotal - (7 * Desconto):.2f}")

else:
    print(f"O valor total SEM o desconto é: R${valorTotal:.2f}")
    print(f"O valor total COM desconto é: R${valorTotal - (11 * Desconto):.2f}")