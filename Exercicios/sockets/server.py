#!/usr/bin/python3

import sys
import socket
import select
import json
import base64
import csv
import random
from common_comm import send_dict, recv_dict, sendrecv_dict

# from Crypto.Cipher import AES

# Dicionário com a informação relativa aos clientes
users = {}
clients = []


# return the client_id of a socket or None
def find_client_id(client_sock):
	for id in users:
		if users[id]["socket"] == client_sock:
			return id
	return None


# return the client_id of a socket or None
def find_client_socket(client_sock):
	if client_sock in clients:
		return client_sock
	return None


# Função para encriptar valores a enviar em formato json com codificação base64
# return int data encrypted in a 16 bytes binary string and coded base64
def encrypt_intvalue(client_id, data):
	# cipher = AES.new(cipherkey, AES.MODE_ECB, "UTF-8")
	# data_encrypt = cipher.encrypt( bytes("%16d" % data))
	# data_encoder = str(base64.b64decode(data_encrypt))
	# return data_encoder
	return None


# Função para desencriptar valores recebidos em formato json com codificação base64
# return int data decrypted from a 16 bytes binary string and coded base64
def decrypt_intvalue(client_id, data):
	# cipher = AES.new(cipherkey, AES.MODE_ECB, "UTF-8")
	# data_decoder = base64.b64decode(data)
	# data_decrypt = cipher.decrypt(data_decoder)
	# return int(str(data_decrypt, "utf-8"))
	return None


# Incomming message structure:
# { op = "START", client_id, [cipher] }
# { op = "QUIT" }
# { op = "NUMBER", number }
# { op = "STOP" }
#
# Outcomming message structure:
# { op = "START", status }
# { op = "QUIT" , status }
# { op = "NUMBER", status }
# { op = "STOP", status, min, max }


# Suporte de descodificação da operação pretendida pelo cliente
def new_msg(client_sock):
	request = recv_dict(client_sock)  # read the client request
	print("Chegou nova mensagem: " + str(request))

	response = None
	# iniciatlize response variable

	# detect the operation requested by the client
	# execute the operation and obtain the response (consider also operations not available)
	if request["op"] == "START":
		response = new_client(client_sock, request)  # search for new client and starts
	elif request["op"] == "QUIT":
		response = quit_client(client_sock, request)  # quit client
	elif request["op"] == "NUMBER":
		response = number_client(client_sock, request)  # number operation
	elif request["op"] == "STOP":
		response = stop_client(client_sock, request)  # stop operation
		print("Stop done, clearing client...")
		clean_client(client_sock)  # clean client
	else:
		response = {"op": request["op"], "status": False, "error": "Invalid operation!"}  # not an operation

	send_dict(client_sock, response)  # send the response to the client


# operação START
def new_client(client_sock, request):
	response = ""
	chiper = None

	client_id = request["client_id"]
	if "chipher" in request:
		chiper = request["chipher"]

	print("De client: " + str(client_id))

	# verify the appropriate conditions for executing this operation
	if client_id not in users:
		print("client não está na lista")
		print("a adicionar client a lista de users...")
		user = dict({"socket": client_sock, "cipher": chiper, "numbers": []})
		users[client_id] = user
		print("adicionado: " + str(client_id) + " aos users: " + str(user))
		response = {"op": "START", "status": True}
	else:
		print("client está na lista")
		response = {"op": "START", "status": False, "error": "Cliente existente"}

	return response


# detect the client in the request
# verify the appropriate conditions for executing this operation
# process the client in the dictionary
# return response message with or without error message


# Suporte da eliminação de um cliente
def clean_client(client_sock):
	cli = find_client_id(client_sock)  # obtain the client_id from his socket and delete from the dictionary

	if cli:  # if cli exists
		print("Apagando user: " + str(cli))
		del users[cli]  # deletes client

		print("users ainda ativos: " + str(users))
		return True

	print("users ainda ativos: " + str(users))
	return False


# Suporte do pedido de desistência de um cliente - operação QUIT
def quit_client(client_sock, request):
	client_sock = find_client_socket(client_sock)  # obtain the client_id from his socket

	# verify the appropriate conditions for executing this operation
	if client_sock:
		client_id = find_client_id(client_sock)
		if client_id:
			print("Apagando client: " + str(client_sock))
			del users[client_id]  # deletes client
			print("Cliente: " + client_id + " removido: " + str(client_sock))

		# return response message with result message
		return {"op": "QUIT", "status": True}
	else:
		# return response message with error message
		return {"op": "QUIT", "status": False, "error": "Cliente inexistente"}


# obtain the client_id from his socket
# verify the appropriate conditions for executing this operation
# process the report file with the QUIT result
# eliminate client from dictionary
# return response message with or without error message

# Suporte da criação de um ficheiro csv com o respectivo cabeçalho
# create report csv file with header
def create_file():
	f = open("report.csv", 'w')  # opens csv file
	header = ['client_id', 'qt_numbers', 'min', 'max']

	with open('report.csv', 'w', encoding='UTF8') as f:
		writer = csv.writer(f)
		writer.writerow(header)


# Suporte da actualização de um ficheiro csv com a informação do cliente e resultado
def update_file(client_id, result):
	result = [client_id] + result

	with open("report.csv", "a+", newline='') as file:
		writer = csv.writer(file)  # writes
		writer.writerow(result)


# update report csv file with the result from the client

# Suporte do processamento do número de um cliente - operação NUMBER
def number_client(client_sock, request):
	user = find_client_id(client_sock)  # obtain the client_id from his socket
	print("user: " + str(user))
	if user:
		users[user]["numbers"] = list(users[user]["numbers"]) + [request["number"]]
		print("Numeros de " + str(user) + ": " + str(users[user]["numbers"]))
		return {"op": "NUMBER", "status": True}  # process the report file with the SUCCESS result
	else:

		return {"op": "NUMBER", "status": False,
				"error": "Cliente inexistente"}  # process the report file with the FAILURE result


# Suporte do pedido de terminação de um cliente - operação STOP
def stop_client(client_sock, request):
	user = find_client_id(client_sock)  # obtain the client_id from his socket
	if user:
		minimo = 0
		maximo = 0
		if len(users[user]["numbers"]) == 0:
			return {"op": "STOP", "status": False, "error": "Dados insuficientes"}
		elif len(users[user]["numbers"]) == 1:
			minimo = users[user]["numbers"][0]
			maximo = users[user]["numbers"][0]
		else:
			minimo = min(list(users[user]["numbers"]))
			maximo = max(list(users[user]["numbers"]))

		qt_numbers = len(users[user]["numbers"])
		result = [qt_numbers, minimo, maximo]
		update_file(user, result)  # verify the appropriate conditions for executing this operation
		print("min: " + str(minimo) + ", max: " + str(maximo))
		return {"op": "STOP", "status": True, "min": minimo,
				"max": maximo}  # process the report file with the SUCCESS result
	else:
		return {"op": "STOP", "status": False,
				"error": "Cliente inexistente"}  # process the report file with the FAILURE result


def main():
	# validate the number of arguments and eventually print error message and exit with error
	# verify type of of arguments and eventually print error message and exit with error

	if (len(sys.argv) != 2):
		print("Incorrect number of arguments!")
		exit(1)

	port = int(sys.argv[1])

	if (port < 0 or port > 65535):
		print("Incorrect port number!")
		sys.exit(-1)

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("127.0.0.1", port))
	server_socket.listen(10)
	print("Server running")

	create_file()

	while True:
		try:
			available = select.select([server_socket] + clients, [], [])[0]
		# print(available)
		except ValueError:
			# Sockets may have been closed, check for that
			for client_sock in clients:
				if client_sock.fileno() == -1:
					client_sock.remove(client_sock)  # closed
					print("Socket closed exception")
			continue  # Reiterate select

		for client_sock in available:
			# New client?
			if client_sock is server_socket:
				newclient, addr = server_socket.accept()
				clients.append(newclient)
				print("append new client: " + str(newclient));
			# Or an existing client
			else:
				# See if client sent a message
				if len(client_sock.recv(1, socket.MSG_PEEK)) != 0:
					# client socket has a message
					new_msg(client_sock)
				# Or just disconnected
				else:
					print("Cliente disconnected: " + str(client_sock))
					clean_client(client_sock)
					clients.remove(client_sock)
					client_sock.close()
					print("users ainda ativos: " + str(users))
					print("clients ainda ativos: " + str(clients))
					break
			# Reiterate select


if __name__ == "__main__":
	main()
