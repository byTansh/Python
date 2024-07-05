print("Bem vindo a loja do Tiago!\n")

# Primeira função --> Function Escolha serviço
def escolha_servico():
    
    while True:
        
        # Declaração de variavel + input de "Escolha serviço"
        escolherServico = str(input("Entre com o tipo de servico desejado\n"
                                    "DIG - Digitalizacao\n"
                                    "ICO - Impressao Colorida\n"
                                    "IPB - Impressao Preto e Branco\n"
                                    "FOT - Fotocopia\n"
                                    ">> ")).strip().upper()
        
        # Condição 1
        if escolherServico not in ["DIG", "ICO", "IPB", "FOT"]:
            print("Escolha Invalida, entre com o tipo de servico novamente\n")
            continue
        
        # Condição 2
        else:
            
            # Condição 3
            if escolherServico == "DIG":
                custoPP = 1.10
                
            # Condição 4
            elif escolherServico == "ICO":
                custoPP = 1.00
                
            # Condição 5
            elif escolherServico == "IPB":
                custoPP = 0.40
                
            # Condição 6
            else:
                custoPP = 0.20
                
        # Retornar valor de custoPP
        return custoPP

# Segunda função --> Function Número de páginas
def num_pagina():
    
    # Laço de repetição, caso o usuario erre o "Námero de páginas"
    while True:
        
        # Caso o usuario insira um caracter diferente de Int
        try:
            
            # Declaração de variavel + input de "Número de Páginas"
            print("")
            numeroDePaginas = int(input("Entre com o numero de paginas: \n"
                                        ">> "))
            
            # Condição 1
            if numeroDePaginas > 20000:
                print("Nao aceitamos tantas paginas de uma vez. \n"
                      "Por favor, entre com o numero de paginas novamente.\n")
                continue
            
            # Condição 2
            elif numeroDePaginas <= 0:
                print("Numero nao pode ser zero ou negativo \n"
                      "Por favor, entre com o numero de paginas novamente.\n")
                continue
            
            # Condição 3
            else:
                
                # Condição 4
                if numeroDePaginas <20:
                   desconto = 0
                   
                # Condição 5
                elif 20 <= numeroDePaginas < 200:
                   desconto = 0.15
                   
                # Condição 6
                elif 200 <= numeroDePaginas<= 2000:
                    desconto = 0.20
                    
                # Condição 7
                else:
                    desconto = 0.25
                totalComDesconto = numeroDePaginas * (1 - desconto)
                
                # Retornar Valor de TotalComDesconto
                return totalComDesconto
        
        # Print error caso o usuario insira um caracter diferente de Int
        except ValueError:
            print("Entrada invalida, inserir somente numeros")
            
# Terceira função --> Function Serviços Extras
def servico_extra():
    
    # Laço de repetição, caso o usuario erre o "Serviço Extra"
    while True:
        
        # Declaração de variavel + input de "Serviço Extra"
        print("")
        extra = int(input("quer adicionar algum servico?\n"
                          "1 - encadernacao simples - R$ 15.00\n"
                          "2 - encadernacao capa dura - 40.00\n"
                          "3 - nao desejo mais nada\n"
                          ">> "))
        
        # Condição 1
        if  extra not in [1,2, 3]:
             print("opcao invalida")
             continue
         
        # Condição 2
        else:
            
            # Condição 3
            if extra == 1:
                valorServiçoExtra = 15.00
                
            # Condição 4
            elif extra == 2:
                valorServiçoExtra = 40.00
                
            # Condição 5
            else:
                valorServiçoExtra = 0.00
                
        # Retornar Valor de ValorServiçoExtra
        return valorServiçoExtra
    
# Quarta função --> Function Main --> Calculo do preço total
def main():
    
    # Declaração de variaveis para calculo final
    eServico = escolha_servico()
    nPaginas = num_pagina()
    sExtra = servico_extra()
    
    # Mostrar valores das opções escolhidas
    valorTotal = eServico * nPaginas + sExtra
    print("")
    # Print do valor total
    print(f"Total: R${valorTotal:.2f} (serviço: {eServico:.2f} * páginas: {nPaginas:.2f} + extra: {sExtra:.2f})")


main()