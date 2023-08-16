#Exer 1
def preenche_lista(l: list) -> None:
    while True:
        valor = input("\nPreencha sua lista: ")
        if valor == 'True':
            valor = True
        elif valor == 'False':
            valor = False
        else: 
            if valor.replace('.', '', 1).replace('-', '', 1).isdigit():
                if '.' in valor:
                    valor = float(valor)
                elif '-' in valor:
                    valor = int(valor)
                else:
                    valor = int(valor)
        l.append(valor)
        if valor == '':
            l.pop(-1)
            break   

#Exer 2
def exibe_lista(l: list) -> None:
    print("\n----- Exer 2 -----")
    print(f"\nSua Lista = {l}")

#Exer3
def conta_elementos(l: list) -> list:
    contador = 0
    print("\n----- Exer 3 ------\n")
    for i in l:
        contador += 1
    return f"há {contador} elemento(s) na sua lista."

#Exer4
def retorna_indice(l: list, elemento: int) -> list:
    print("\n----- Exer 4 ------\n")
    for i, e in enumerate(l):
        if e == elemento:
            return f"o índice do elemento é: {i}"
        return f"{-1}, não há este índice na lista :("

#Exer5
def busca(l: list, elemento) -> int:
    print("\n----- Exer 5 ------\n")
    busc = 0
    for i in l:
        if str(i) == elemento:
            busc += 1
    return f"achamos {busc} elemento procurado na lista!"

#Exer 6
def conta_inteiro(l: list) -> list:
    print("\n----- Exer 6 -----\n")
    itr = 0
    for i in l:
        if str(i).isdigit():
            itr += 1
    return f"há {itr} inteiro(s) na lista."

#Exer 7
def conta_string(l: list) -> list:
    print("\n----- Exer 7 -----\n")
    stg = 0
    for i in l:
        if str(i) == i:
            stg += 1
    return f"Quantidade de strings na lista: {stg}"

#Exer8
def conta_boolean(l: list) -> list:
    print("\n----- Exer 8 -----\n")
    bol = 0
    for i in l:
        if i in (True, False):
            bol += 1
    return f"Quantidade de boolean na lista: {bol}"


#Exer 9
def conta_float(l: list) -> list:
    print("\n----- Exer 9 -----\n")
    flt = 0
    for i in l:
        if '.' in str(i):
            flt += 1
    return f"Quantidade de float(s) na lista: {flt}"

#Exer 10
def copia_int(l: list, l2: list) -> None:
    print("\n----- Exer 10 -----\n")
    for i in l:
        if str(i).isdigit():
            l2.append(int(i)) 
    print(f"(Apenas com os inteiros) \n Sua lista2 = {l2}") 