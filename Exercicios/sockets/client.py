#!/usr/bin/python3

import os
import sys
import socket
import json
import base64
from common_comm import send_dict, recv_dict, sendrecv_dict

#from Crypto.Cipher import AES

# Função para encriptar valores a enviar em formato jsos com codificação base64
# return int data encrypted in a 16 bytes binary string coded in base64
#def encrypt_intvalue (cipherkey, data):
	# cipher = AES.new(cipherkey, AES.MODE_ECB, "UTF-8")
	# data_encrypt = cipher.encrypt( bytes("%16d" % data))
	# data_encoder = str(base64.b64encode(data_encrypt))
	# return data_encoder


# Função para desencriptar valores recebidos em formato json com codificação base64
# return int data decrypted from a 16 bytes binary strings coded in base64
#def decrypt_intvalue (cipherkey, data):
	# cipher = AES.new(cipherkey, AES.MODE_ECB, "UTF-8")
	# data_decoder = base64.b64decode(data)
	# data_decrypt = cipher.decrypt(data_decoder)
	# return int(str(data_decrypt, "utf-8"))

# process QUIT operation
def quit_action(client_sock):
	quitOP = sendrecv_dict(client_sock, {"op": "QUIT"})  # returns to the server the quit operation
	validate_response(client_sock, quitOP) # Validation
	print("Saindo do programa")
	client_sock.close() # closes client_sock

# verify if response from server is valid or is an error message and act accordingly
def validate_response(client_sock, response):
	if response["status"] == False:
		print("Error: " + response["error"] + "\n") # returns error message
		quit = sendrecv_dict(client_sock, {"op", "QUIT"}) # returns to the server the quit operation
		validate_response(client_sock, quit) # Validation
		client_sock.close()  # closes client_sock
		print("Saindo do programa!")
		sys.exit(3)

	return None

# Outcomming message structure:
# { op = "START", client_id, [cipher] }
# { op = "QUIT" }
# { op = "NUMBER", number }
# { op = "STOP" }
#
# Incomming message structure:
# { op = "START", status }
# { op = "QUIT" , status }
# { op = "NUMBER", status }
# { op = "STOP", status, min, max }

def menu():
	print("{ op = START}")
	print("{ op = QUIT}")
	print("{ op = NUMBER}")
	print("{ op = STOP}")

# Suporte da execução do cliente
def run_client(client_sock, client_id):
	#START
	print("client running: ")
	while True:
		menu()
		op = input("Enter OP: ")
		op = op.upper()
		print("Trying to send op: " + str(op))

		if op == "START":
			response = sendrecv_dict(client_sock, {"op": op, "client_id": client_id})  # returns to the server the start operation
		elif op == "QUIT":
			response = quit_action(client_sock)

			sys.exit(4) # program closes if #quit_action's function is used
		elif op == "NUMBER":
			try:
				number = int(input("Enter a number: "))
				response = sendrecv_dict(client_sock, {"op": op, "number": number})
			except:
				print("Value entered is not a number! try again")
		elif op == "STOP":
			response = sendrecv_dict(client_sock, {"op": op})
		else:
			print("Operação inexistente")

		print("response from server: " + str(response))
		validate_response(client_sock, response) # Validation


def main():
	# validate the number of arguments and eventually print error message and exit with error
	# verify type of of arguments and eventually print error message and exit with error

	if len(sys.argv) < 3 or len(sys.argv) > 4:
		print("Incorrect number of arguments!")
		print("Saindo do programa!")
		sys.exit(1)

	port = int(sys.argv[2])

	hostname = '127.0.0.1'
	
	if (len(sys.argv) == 4): #python3 client.py hugo 100 10.0.256.2 <-
		hostname = sys.argv[3]

	if(port < 0 or port > 65535): 
		print("Incorrect port number!")
		print("Saindo do programa!")
		sys.exit(2)

	client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_sock.connect((hostname, port))
	print("client connecting...")

	run_client(client_sock, sys.argv[1])

	client_sock.close()
	print("Saindo do programa!")
	sys.exit(0)

if __name__ == "__main__":
    main()
