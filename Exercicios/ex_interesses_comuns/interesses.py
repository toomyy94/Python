def alinea_A(interessesPessoa):
    dictInteressesComuns = {}
    lstPessoas = list(interessesPessoa.keys())
    lstlstInteressesPessoas = list(interessesPessoa.values())

    for i in range(0, len(interessesPessoa)-1):
        for j in range(1, len(interessesPessoa)):
            if j == i:
                continue

            tmpLstInteressesComuns = []

            for interesse in lstlstInteressesPessoas[i]:
                if (interesse in lstlstInteressesPessoas[j]):
                    tmpLstInteressesComuns.append(interesse)

            dictInteressesComuns[(lstPessoas[i], lstPessoas[j])] = tmpLstInteressesComuns

    return dictInteressesComuns

def alineaB(dictInteressesComuns):
    lstLenInteresses = []

    for lstInteresses in list(dictInteressesComuns.values()):
        lstLenInteresses.append(len(lstInteresses))

    return max(lstLenInteresses)

def alineaC(dictInteressesComuns, lenMaxInteresses):
    dictPairsMaxInteresses = {k: dictInteressesComuns[k] for k in sorted(dictInteressesComuns)}
    lstKeystoRemove = []

    for key in dictPairsMaxInteresses.keys():
        if len(dictPairsMaxInteresses[key]) != lenMaxInteresses:
            lstKeystoRemove.append(key)

    for i in range(len(lstKeystoRemove)):
        dictPairsMaxInteresses.pop(lstKeystoRemove[i])

    return dictPairsMaxInteresses

def alineaD(dictInteressesComuns):
    dict2Interesses = {k: v for k, v in dictInteressesComuns.items() if len(v) == 1}
    return dict2Interesses


if __name__ == '__main__':
    interessesPessoa = {
        'Paulo': ['a', 'b'],
        'Teresa': ['a', 'c', 'd'],
        'Anna': ['a', 'b', 'd'],
        'Alberto': ['a', 'd'],
        'Frank': ['a', 'c', 'd']
    }

    dictInteressesComuns = alinea_A(interessesPessoa)
    print(dictInteressesComuns)

    lenMaxInteresses = alineaB(dictInteressesComuns)
    print(lenMaxInteresses)

    dictPairsMaxInteresses = alineaC(dictInteressesComuns, lenMaxInteresses)
    print(dictPairsMaxInteresses)

    print(alineaD(dictInteressesComuns))
