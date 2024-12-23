from random import randint

##while loop

numero_random = 0

while numero_random < 11:
    print(numero_random)
    numero_random = randint(5, 10)
    if(numero_random == 5):
        print("Numero random é igual a 5. Saindo...")
        break

        rand

print("---------------------")

##for loop
frase = "frase"
lista = [4,3,2,1]

for caracter in range(0, len(frase)):
    print(frase[caracter])

#for abaixo igual ao de cima
#for i in range(0, len(frase)):
#    print(frase[i])

for numero_da_lista in lista:
    print(numero_da_lista)

for y in range(1, 10):
    print("ola")

print("------------- Exercicio -----------------")
print("Quantas vezes corre a linha")

n = 21
count = 0

for i in range(0, n):
    for j in range(1, n, 2):
        count+=1

print(n*n/2) #work on this
print(count)

