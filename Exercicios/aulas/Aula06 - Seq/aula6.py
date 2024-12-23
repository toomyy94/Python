print("Ex2:")
print("")

lst = []


def funcao1():
	print("Quebre o ciclo fazendo Enter")
	print("")
	while True:
		n = input("Número?")
		if n == '':
			break
		lst.append(n)
	print(lst)


funcao1()


v = float(input("Nº v?"))


def countLower(lst, v):
	# v = input("Nº v?")
	count = 0
	i = 0
	while i < len(lst):
		if float(lst[i]) < v:  # IndexError: list index out of range NUNCA FAZER <= LEN, FAZ SEMPRE < LEN!!!


			count +=1
		i +=1
	print("Exitem ", count, " elementos da lista lst que são inferiores ao valor v")


countLower(lst, v)


def minmax(lst):
	min = lst[0]
	max = lst[0]
	r = 0
	while r < len(lst) - 1: #TOMAS: Adicionei o -1 pq na ultima iteração ias aceder ao r+1 e não existia, daí o index out of range
		if lst[r+1] > lst[r]:   #IndexError: list index out of range
			max = lst[r+1]
		elif lst[r+1] < lst[r]:
			min = lst[r+1]
		r +=1
	print("Máx é ", max)
	print("Min é ", min)


minmax(lst)


print("Ex4:")
print("")

teams = []
allMatches = []


def Fut():
	e = 0
	totalEquipas = 0
	print("Quebre ciclo de equipas fazendo Enter")
	while True:
		t = input("Equipa?")
		teams.append(t)
		totalEquipas +=1 # TOMAS: n precisas disto é o len(teams)
		e += 1 # TOMAS: n precisas disto é o len(teams)
		if t == '':
			break
	# while e < len(teams): #TOMAS: n percebi o e é fixo dentro do while, nunca vai sair daqui
	# apaguei o que estava aqui
	for i in range(0, len(teams)-1):
		for j in range(0, len(teams)-1):
			if i != j :
				allMatches.append("["+teams[i] + ", " + teams[j]+"]")

	print(allMatches)


Fut()
		
	
	
		
	




















