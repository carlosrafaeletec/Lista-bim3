from biblioteca import *
lista = []  
lista2 = []

while True:
    print("\nEscolha um Exercicio da Lista: \n")
    print("1 - Preencher uma lista")
    print("2 - exibir a lista")
    print("3 - Contar os elementos")
    print("4 - Retornar o índice")
    print("5 - Buscar um elemento da lista")
    print("6 - Contar os inteiros")
    print("7 - Contar as Strings")
    print("8 - Contar os Booleans")
    print("9 - Conta os Floats")
    print("10 - Copiar os inteiros para uma lista2")
    print("0 - Sair do programa")
    op = input("\nDigite o número da opção desejada: ")

    match op:
        case "1":
            preenche_lista(lista)

        case "2":
            exibe_lista(lista)

        case "3":
            ex3 = conta_elementos(lista)
            print(ex3)

        case "4":
            ex4 = retorna_indice(lista, 12)
            print(ex4)

        case "5":
            elemento = input("Digite o elemento procurado: ")
            ex5 = busca(lista, elemento)
            print(ex5)

        case "6":
            ex6 = conta_inteiro(lista)
            print(ex6)

        case "7":
            ex9 = conta_string(lista)
            print(ex9)

        case "8":
            ex8 = conta_boolean(lista)
            print(ex8)
            
        case "9":
            ex9 = conta_float(lista)
            print(ex9)

        case "10":
            copia_int(lista, lista2)

        case "0":
            print("Desligando...")
            break
        case _:
            print("\n Opção inválida. Por favor, tente novamente.")
