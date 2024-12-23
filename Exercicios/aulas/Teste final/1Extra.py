numero = 123456789
def validarTel(numero):
	numero = str(numero)
	if numero[0] == "+" and len(numero) >= 4 and numero[1:].isnumeric()==True:
		print("Válido!")
	elif numero.isnumeric()==True and len(numero) >= 3:
		print("Válido!")
	else:
		while numero[0].isalpha() or len(numero) < 3 or numero[1:].isnumeric()==False:
			numero = input("Telefone?")
                
                #estou a tentar que corra a 100%    Consegui ??  
                #Não, os casos com +xy não fazem nada
validarTel(numero)

def menu():
	
	print("(R)egistar chamada")
	print("(L)er Ficheiro")
	print("Listar (C)lientes")
	print("(F)atura")
	print("(T)erminar")
	
	op = input("Opção?").upper()
	
	if op == "R":
	
		torigem = input("Telefone origem?")
		validarTel(torigem)
		
		tdestino = input("Telefone destino?")
		validarTel(tdestino)
		
		tempo = input("Duração(s)?")
		
		
	if op == "L":
		
		ficheiro = input("Ficheiro?")
		with open (ficheiro, "r") as fileobj:
			#for line in fileobj:
			#	print (line)
			print("Ficheiro aberto!")
	
	if op == "C":
		
		lst = []
		#como implemento a opção L aqui para não ter que fazer o que está lá outra vez?
		fin = open('chamadas1.txt')
		for line in fin:
			line.strip("")
			line.strip("\t")
			lst.append(line[0:9])
		lst = set(lst)
		print("Clientes:", sorted(lst))
	
	#Dá-me: Clientes: ['913862602', '914293467', '919274650', '930930597', '934863725', '939999868', '960373347', '961393096', '962613058', '963970864']
		
		fin.close()
	
	
	if op == "F":
		
		cliente = input("Cliente?")
		fin = open('chamadas1.txt')
		print("Destino:", "             Duração:", "   Custo:")
		for line in fin:
			line = line.replace("\t","    ")
			if line[0:9] == cliente:
				custototal1 = 0
				custototal2 = 0
				custototal3 = 0
				custototal4 = 0
				if line[13] == "+":
					custo = 0.8*(int(line[26:31])/60)
					custototal1 += custo
					print (line[13:26], "       ", line[26:31], "     ", custo)
				elif line[13] == "2":
					custo = float(0.02*(int(line[26:31])/60))
					custototal2 += custo
					#print ("{} {} {} {} {2.2f}".format(line[13:26], "          ", line[26:31], "     ", custo))
					#tentei como está acima e deu um erro novo
					print (line[13:26], "       ", line[26:31], "     ", custo)
				elif line[13]==line[14]:
					custo = 0.04*(int(line[26:31])/60)
					custototal3 += custo
					print (line[13:26], "          ", line[26:31], "     ", custo)
				else:
					custo = 0.1*(int(line[26:31])/60)
					custototal4 += custo
					print (line[13:26], "          ", line[26:31], "     ", custo)
				
		print("Custo total:", custototal1+custototal2+custototal3+custototal4)
		#Está a dar mal custo total!
				
	if op == "T":
		print("Escolheste terminar o programa!")
	
menu()








