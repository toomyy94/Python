dic = {}

dic["f"] = 1
dic["s"] = 2
dic["t"] = 3

print(dic)
print(len(dic))

print(dic["f"])

del dic["s"]
print(dic)


def changeDict(dictio):
    dictio["t"] = 10


changeDict(dic)
print(dic)