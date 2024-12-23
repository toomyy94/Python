def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def readFileToStringList(filename):
    linesList = []

    with open(filename, "r") as f:
        for line in f:
            linesList.append(line)

    return linesList


def ex1():
    filename = "nums.txt"
    linesList = readFileToStringList(filename)
    num_sum = 0

    for num in linesList:
        if is_float(num):
            num_sum += float(num)
        else:
            print("invalid file: " + filename)
            exit(-1)

    print(num_sum)


print("Ex1:")
ex1()


def chomp(s):
    if s.endswith('\n'):
        return s[:-1]
    else:
        return s


def notaFinal(tuplo_aluno):
    nota_final = 0

    for x in tuplo_aluno[:3]:
        if is_float(x):
            nota_final += float(x)

    return round(nota_final / len(tuplo_aluno[2:]), 1)


def sort_lista_tuplos(listaTuplos):
    listaTuplos.sort(key = lambda x: x[0])
    return listaTuplos


def listTuplosToString(lista_completa):
    listaOrdenada = ""

    for tuplo in lista_completa:
        for element in tuplo:
            listaOrdenada += (str(element) + "\t")

        listaOrdenada += "\n"

    return listaOrdenada


def write_formatted_csv(filename, lista_completa):
    f = open(filename, "w")
    f.write(listTuplosToString(lista_completa))
    f.close()


def ex3():
    filename = "school_inventado.csv"
    linesList = readFileToStringList(filename)
    sum_notas = 0
    lista_completa_alunos = []

    for linha in linesList:
        linha_aluno = linha.split("\\t")
        linha_aluno[len(linha_aluno)-1] = chomp(linha_aluno[len(linha_aluno)-1])

        aluno = tuple(linha_aluno)
        lista_completa_alunos.append(aluno)

    print("3a)")
    print(lista_completa_alunos)
    print("3b)")
    print(notaFinal(lista_completa_alunos[0]))
    print(notaFinal(lista_completa_alunos[1]))
    print("3c)")
    print(sort_lista_tuplos(lista_completa_alunos))
    print("Ex4")
    write_formatted_csv("sorted_list.txt", sort_lista_tuplos(lista_completa_alunos))
    print("ver ficheiro criado sorted_list.txt!")


print("----------------------")
print("Ex3:")
ex3()

