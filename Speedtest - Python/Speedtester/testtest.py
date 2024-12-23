# def func(lst1, lst2):
#     lst = []
#     for x in lst1:
#         for s in lst2:
#             lst.append(x in s)
#     return lst
#
# a = ["1","2","3"]
# b=["3","1","22"]
#
# c = func(a,b)
#
# print(c)
#
# def func2(lst1, lst2):
#     return [ x in s for x in lst1 for s in lst2]
#
# d = ["1","2","3"]
# e = ["3","1","22"]
#
# f = func2(a,b)
# print(f)
#
# def load(lst):
#     l=[]
#     n = 0
#     for x in lst:
#         v = int(x)
#         print(v, end=',')
#         l.append(v)
#         if v > 0:
#             n += 1
#     print()
#     return len(l), n, l
#
# li = ["10", "8", "5", "9"]
#
# k1, k2, k = load(li)
# print(k1)
# print(k2)
# print(sum(k))
#
# def reverseStr(s):
#     if len(s) < 1 :
#         return s
#     else:
#         return reverseStr(s[1:]) + s[0]
#
# print(reverseStr("papagaio"))

# def morePop(countries, N):
#     lst = []
#     for country in countries:
#         if country[3] > N:
#             lst.append(((country[3], country[0])))
#     return lst
#
#
#

# print(morePop(countries, 10000))

# def ex2():
#
#     taxa = 0.0
#     imposto = 0.0
#     deducao = 0.0
#     rendimento = 0.0
#
#
#     x = "init"
#     while x != "":
#         x = input("Rendimento? ")# Income?
#         if x != "":
#             num = float(x)
#             rendimento = num
#
#             if num < 10000:
#                 taxa = 5
#                 deducao = 0
#             elif num < 20000:
#                 taxa = 10
#                 deducao = 500
#             else:
#                 taxa = 15
#                 deducao = 1500
#
#             imposto = ((taxa/100) * rendimento) - deducao
#             print("{:.2f}".format(imposto))
#
#
# ex2()

def loadFile(filename):
    lst = []
    f = open(filename)
    count = 0
    for line in f:
        count += 1
        if count == 1 or len(line) < 2:
            continue
        else:
            line = line.rstrip()
            print(line)
            lista = (line.split(","))
            lst.append( tuple(lista) )

    return  lst

def sortCountries(countries):
    countriesDens = []

    for c in countries:
        c = list(c)
        dens = (c[3]/c[2])
        c.append(dens)
        c = tuple(c)
        countriesDens.append(c)

    countriesDens = sorted(countriesDens, key=lambda x: x[4], reverse=True)

    return countriesDens

def portfolioValue(stocks, cart1):
    soma = 0
    for k,v in cart1.items():
        for k2,v2 in stocks.items():
            if k == k2:
                soma = soma + (v*v2)
            else:
                continue

    soma = soma + cart1["EUR"]
    return soma

def transaction (stocks, Q, E, C1, C2):
    assert Q >= 0
    assert E in stocks
    assert "EUR" in C1
    assert "EUR" in C2

    if C1[E] < Q:
        return "NO-STOCK"
    else:
        if stocks[E] * Q > C2["EUR"]:
            return "NO-MONEY"
        else:
            C1[E] = C1[E] - Q
            try:
                C2[E] = C2[E] + Q
            except:
                C2[E] = Q

            C1["EUR"] = C1["EUR"] + (stocks[E] * Q)
            C2["EUR"] = C2["EUR"] - (stocks[E] * Q)

    return "OK"

def stockholders(portfolios):
    dic = {}
    lst = []

    print ("ola")
    for k, v in portfolios.items():
        for k2, v2 in v.items():
            lst.append(k)
            lst.append(k2)
        print(lst)
        lst.clear()


    return dic

def numberOfDigits(n):
    if n < 10:
        return 1
    else:
        return 1 + numberOfDigits(n/10)

def score(guess, secret):
    assert len(guess) == len(secret)
    bull = 0
    cow = 0

    for g in range(0, len(guess)):
        for s in range(0, len(secret)):
            if g == s and guess[g] == secret[s]:
                bull +=1
            elif g == s and guess[g] != secret[s] and secret[s] in guess:
                cow += 1

    return (bull, cow)




if __name__ == "__main__":

    print(score('1234', '4271'))
    print(score('3449', '3904'))
    print(score('12345', '57213'))
    print(score('ALADA', 'MARIA'))
    print(score('827323', '728371'))

    countries = [
        ("Grenada", "Na",344.0, 108825),
        ("Kenya", "AF", 581834.0,47564296),
        ("Liechtenstein", "EU", 160.0, 38380)]

    cart1 = {'CSCO': 10, 'EUR': 1000.0, 'IBM': 10}
    cart2 = {'EUR': 2000.0, 'IBM': 10, 'QCOM': 10, 'TSLA': 10}

    stocks = {
        "ALU": 3, "CSCO":3, "AMZN": 3, "HPQ": 3,"TSLA":3, "IBM": 3,'QCOM': 3
    }

    #print(loadFile("file"))
    #print(sortCountries(countries))
    print("aqui")
    print(portfolioValue(stocks, cart1))
    print(portfolioValue(stocks, cart2))
    print(transaction(stocks, 5, 'IBM', cart1, cart2))

    cart1 = {'CSCO': 20, 'EUR': 1000.0, 'IBM': 10}
    cart2 = {'EUR': 2000.0, 'IBM': 5, 'QCOM': 10, 'TSLA': 10}
    stocks = {
        "ALU": 4.04, "CSCO":200, "AMZN": 627.13, "HPQ": 12.47, "IBM": 140.5
    }

    print(transaction(stocks, 10, 'CSCO', cart1, cart2))

    cart1 = {'CSCO': 20, 'EUR': 1000.0, 'IBM': 10}
    cart2 = {'EUR': 2000.0, 'IBM': 5, 'QCOM': 10, 'TSLA': 10}
    stocks = {
        "ALU": 4.04, "CSCO":200, "AMZN": 627.13, "HPQ": 12.47, "IBM": 140.5
    }
    print(transaction(stocks, 30, 'CSCO', cart1, cart2))

    cart1 = {'CSCO': 20, 'EUR': 1000.0, 'IBM': 10}
    cart2 = {'EUR': 2000.0, 'IBM': 5, 'QCOM': 10, 'TSLA': 10}
    stocks = {
        "ALU": 4.04, "CSCO":200, "TSLA":1300, "AMZN": 627.13, "HPQ": 12.47, "IBM": 140.5
    }
    print(transaction(stocks, 4, 'TSLA', cart2, cart1))

    cart1 = {'CSCO': 20, 'EUR': 1000.0, 'IBM': 10}
    cart2 = {'EUR': 2000.0, 'IBM': 5, 'QCOM': 10, 'TSLA': 10}
    stocks = {
        "ALU": 4.04, "CSCO":200, "TSLA":1300, "AMZN": 627.13, "HPQ": 12.47, "IBM": 140.5
    }
    print(transaction(stocks, 5, 'TSLA', cart2, cart1))

    cart1 = {'CSCO': 20, 'EUR': 1000.0, 'IBM': 10}
    cart2 = {'EUR': 2000.0, 'IBM': 5, 'QCOM': 10, 'TSLA': 10}

    portfolios = {}
    portfolios["john"] = cart1
    portfolios["anna"] = cart2
    print(stockholders(portfolios))
    print(numberOfDigits(1234))

