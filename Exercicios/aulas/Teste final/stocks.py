# Using formatters to give 6
# spaces to each set of values
# print("{:6d} {:6d} {:6d} {:6d}"
# .format(i, i ** 2, i ** 3, i ** 4))

def printStocks(stocks):
    for line in stocks:
        print("{:12s} {:12s} {:12.2f} {:12.2f} {:12d} {:7.2f}%".format(line[0], line[1], line[2], line[3], line[4], ((line[3]/line[2])*100 - 100)))


# Cada tuplo = (empresa, cidade, abertura, fecho, volume)
stocks = [
    ('INTC', 'London', 34.249, 34.451, 1792860),
    ('TSLA', 'London', 221.33, 229.63, 398520),
    ('EA', 'Paris', 72.63, 68.98, 1189510),
    ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
    ('TSLA', 'Paris', 217.35, 217.75, 252500),
    ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
]

stocks2 = sorted(stocks, key = lambda t: (t[0], -t[4])) #Tomas
printStocks(stocks2)

print("")
print("Paris:")

def paris(): # Tomas
    stocks3 = []
    for line in stocks:
        if line[1] == "Paris":
            tuple = (line[0], line[1], line[2], line[3], line[4])
            stocks3.append(tuple)
    printStocks(stocks3)
paris()

#Tomas
print("")
print("Ficheiro:")
def load(fileobj):
    stocks4 = []
    with open("stocks.txt", "r") as fileobj:
        for line in fileobj:
            if line is None:
                break
            line = line.replace("\n", "")
            lista = line.split("\t")
            lista[2] = float(lista[2])
            lista[3] = float(lista[3])
            lista[4] = int(lista[4])
            tupleS = tuple(lista)
            stocks4.append(tupleS)
        return stocks4



stocks4 = load("stocks.txt")
printStocks(stocks4)


assert type(stocks4)==list
assert type(stocks4[0])==tuple
assert len(stocks4[0])==5
assert type(stocks4[0][2])==float
assert type(stocks4[0][4])==int
print("FIM")
