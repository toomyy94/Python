print("primeira frase")

print('segunda frase')

print("uma frase \"entre aspas\"!")

frase = "terceira e ultima frase"
print(frase[0])
print(frase[:9])
print(frase[9:18])
print(frase[18:])

print(len(frase))
print(1234)
##a proxima linha dá erro pq 1234 ainda n é string / não posso aceder á posição/caracter [1]
##print(1234[1])
print(str(1234)[1])
print(frase.upper())
print(frase.lower())

name = input("Escreve o teu nome: ")
print("O teu nome é " + "%s" %(name))

numero = 180.123
numero2 = 150.123
print(("%6.2f"%numero).rjust(20))
print('{:6.1f}, {:6.1f}, {:s}'.format(numero, numero2, name))
