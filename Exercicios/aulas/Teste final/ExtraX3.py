print("Ex3")


def menu():
    print("")
    print("(I)nserir itens")
    print("(F)aturar")
    print("(S)air")
    op = input("Opção?").upper()
    return op


def main():
    op = ""
    while op != "S":
        op = menu()

        if op == "I":
            cod = input("Código do produto?")
            fileobj = open("hipermercado.txt", 'r')
            while cod != 0:
                for line in fileobj:
                    line = line.split()

                    if cod == line[0]:            #SÓ ESTOU A CONSEGUIR ACEDER A UM DIGITO DE CADA VEZ
                        print(line[1], line[0])

                    if cod == 0:
                        break

        elif op == "S":
            with open("Vendas.txt", "w") as ficheiroV:
                a=0

            #with open("StockOut.txt", "w") as fileobj:
                #???



        elif op =="F":
            b=0

main()


