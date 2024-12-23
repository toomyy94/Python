print("Ex1")

def validarTelefone():
    telefone = input("nº telefone?")
    telefone = str(telefone)
    for l in telefone:

        if l.isnumeric()==False:
            #if "+" == telefone[0]:       #PROBLEMA!!
             #   pass
            print("nº inválido, só pode ter números")
            telefone = input("nº telefone?")

    if len(telefone) < 3:
        print('nº inválido, tem de ter no min 3 dígitos')
        telefone = input("nº telefone?")
    else:
        print(telefone)

def lerFicheiro():
    ficheiro = input("Ficheiro?")
    fileobj = open(ficheiro, 'r')  # open for reading

def menu():
    print()
    print("(R)egistar chamada")
    print("(L)er (F)icheiro")
    print("(L)istar Clientes")
    print("(F)atura")
    print("(T)erminar")
    op = input("Opção?").upper()
    return op


def main():
    op = ""
    while op != "T":
        op = menu()
        if op =="T":
            print("Terminado")
        elif op == "R":
            norigem = input("Telefone origem?")
            ndestino = input ("Telefone destino")
            validarTelefone(norigem)
            validarTelefone(ndestino)
        elif op == "LF":
            lerFicheiro()
        elif op == "L":
            listaOrigem = []
            fin = open("chamadas1.txt")
            fin = fin.split()             #problemas!!!!
            for line in fin:
                listaOrigem.append(line[0])
            listaOrigem = set(listaOrigem)
            print("Clientes:", listaOrigem)
        elif op == "F":
            cliente = input("Nº cliente?")
            listaDestino = []
            fin = open("chamadas1.txt")
            fin = fin.split()
            for line in fin:
                if line[0] == cliente:
                    listaDestino.append(line [1], line[2])
                custo = line [2] * 0.1
                Custo = sum(custo)

                #opção por terminar








main()


