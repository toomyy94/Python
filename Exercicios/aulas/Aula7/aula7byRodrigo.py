print("Ex3")


def lerFicheiro(filename):
    lst = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            l = line.split("\t")
            for word in l:
                if word.endswith("\n"):
                    word = word[:-1]
                    l[len(l)-1]= word

            t = tuple(l)
            lst.append(t)

    return lst


macacos = lerFicheiro("school.csv")
print(macacos)