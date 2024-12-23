# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

def alinea_A():
    userCarDict = {}

    ep1File = open("C:/Users/XDLTA54/Desktop/ep1.csv", 'r')  # open for reading
    for line in ep1File:
        line = line.replace('\n', '')
        carsList = []

        carsList.append(line.split(';')[0])

        if (line.split(';')[2] in userCarDict):
            userCarDict[line.split(';')[2]].append(line.split(';')[0])
        else:
            userCarDict[line.split(';')[2]] = carsList

    ep1File.close()

    return userCarDict


def alinea_B(userCarDict):

    lstMatriculasSorted = []
    userCarDictSorted = dict(sorted(userCarDict.items()))
    for matriculas in userCarDictSorted.values():
        matriculasSorted = sorted(matriculas)
        lstMatriculasSorted.append(matriculasSorted)

    for i in range(len(userCarDict)):
        userCarDict[list(userCarDictSorted.keys())[i]] =  lstMatriculasSorted[i]

    return dict(sorted(userCarDict.items()))

def alinea_C(userCarDict):
    return userCarDict

def alinea_D(matricula):
    try:
        if matricula.split('-')[0].isdigit() & matricula.split('-')[1].isalpha() & matricula.split('-')[2].isdigit():
            return True
        else:
            return False
    except:
        return False

def alinea_E(parque):
    while True:
        matricula = input('Matricula? ')
        if alinea_D(matricula):
            break

    while True:
        duracao = input('Duracao? ')
        if duracao.isdigit():
            break

    parque.append((matricula, duracao))

    return parque

def alinea_F(parque):

    parqueFile = open("parque.csv", 'w+', encoding='utf-8')  # open for reading
    for tuplo in parque:
        parqueFile.write(str(tuplo) + ';')

    parqueFile.close()
    return 'Ficheiro Gravado com sucesso'

def alinea_H():
    print('Opcoes disponiveis:')
    print('0 - Terminar')
    print('1 - Ler ficheiro de cliente')
    print('2 - Imprimir clientes ordenados')
    print('3 - ostrar matriculas por cliente')
    print('4 - dicionar acesso ao parqu')
    print('5 - Gravar acessos ao parqu')
    print('6 - Gerar fatura para um cliente')

if __name__ == '__main__':
    parque = []

    while True:
        opcao = input('Opcao ? ')
        if(opcao == str(0)):
            exit(0)
        elif(opcao == str(1)):
            userCarDict = alinea_A()
            print(userCarDict)
        elif(opcao == str(2)):
            print(alinea_B(userCarDict))
        elif(opcao == str(3)):
            print(alinea_C(userCarDict))
        elif(opcao == str(4)):
            print(alinea_E(parque))
        elif(opcao == str(5)):
            print(alinea_F(parque))
        elif(opcao == str(6)):
            print('TODO')














