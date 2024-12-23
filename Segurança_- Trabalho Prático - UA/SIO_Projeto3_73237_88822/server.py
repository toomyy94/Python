import asyncio
import json
import base64
import argparse
import coloredlogs, logging
import re
import os
import PyKCS11
import binascii
from aio_tcpserver import tcp_server

import random
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger('root')

STATE_CONNECT = 0
STATE_OPEN = 1
STATE_DATA = 2
STATE_CLOSE= 3

#GLOBAL
storage_dir = 'files'

class ClientHandler(asyncio.Protocol):
	def __init__(self, signal):
		"""
		Default constructor
		"""
		self.signal = signal
		self.state = 0
		self.file = None
		self.file_name = None
		self.file_path = None
		self.storage_dir = storage_dir
		self.buffer = ''
		self.peername = ''


		##Challenge-Answer
		self.username = ""
		self.password = ""
		##CC/Certificate authentication
		self.private_key = ''

		# random_option = random.randrange(0,2,1)
		#random_option = 0
		#if random_option == 0:
			# Do CC Authentication
		#	cc_function()
		#elif random_option == 1:
			# Do Certificate Authentication
		#	create_certificate()




	def connection_made(self, transport) -> None:
		"""
		Called when a client connects

		:param transport: The transport stream to use with this client
		:return:
		"""


		self.peername = transport.get_extra_info('peername')
		logger.info('\n\nConnection from {}'.format(self.peername))
		self.transport = transport
		self.state = STATE_CONNECT

	def data_received(self, data: bytes) -> None:
		"""
        Called when data is received from the client.
        Stores the data in the buffer

        :param data: The data that was received. This may not be a complete JSON message
        :return:
        """
		logger.debug('Received: {}'.format(data))
		try:
			self.buffer += data.decode()
		except:
			logger.exception('Could not decode data from client')

		idx = self.buffer.find('\r\n')

		while idx >= 0:  # While there are separators
			frame = self.buffer[:idx + 2].strip()  # Extract the JSON object
			self.buffer = self.buffer[idx + 2:]  # Removes the JSON object from the buffer

			self.on_frame(frame)  # Process the frame
			idx = self.buffer.find('\r\n')

		if len(self.buffer) > 4096 * 1024 * 1024:  # If buffer is larger than 4M
			logger.warning('Buffer to large')
			self.buffer = ''
			self.transport.close()


	def on_frame(self, frame: str) -> None:
		"""
		Called when a frame (JSON Object) is extracted

		:param frame: The JSON object to process
		:return:
		"""
		#logger.debug("Frame: {}".format(frame))

		try:
			message = json.loads(frame)
		except:
			logger.exception("Could not decode JSON message: {}".format(frame))
			self.transport.close()
			return

		mtype = message.get('type', "").upper()

		if mtype == 'OPEN':
			ret = self.process_open(message)
		elif mtype == 'DATA':
			ret = self.process_data(message)
		elif mtype == 'CLOSE':
			ret = self.process_close(message)
		elif mtype == 'USER':
			ret = self.processUser(message)
		elif mtype == 'CHALLENGE':
			ret = self.process_challenge(message)
		elif mtype == 'CC':
			ret = self.process_cc_authentication(message)
		elif mtype == 'CERTIFICATE':
			ret = self.process_certificate(message)
		else:
			logger.warning("Invalid message type: {}".format(message['type']))
			ret = False

		if not ret:
			try:
				self._send({'type': 'ERROR', 'message': 'See server'})
			except:
				pass # Silently ignore

			logger.info("Closing transport")
			if self.file is not None:
				self.file.close()
				self.file = None

			self.state = STATE_CLOSE
			self.transport.close()


	def process_open(self, message: str) -> bool:
		"""
		Processes an OPEN message from the client
		This message should contain the filename

		:param message: The message to process
		:return: Boolean indicating the success of the operation
		"""
		logger.debug("Process Open: {}".format(message))

		if self.state != STATE_CONNECT:
			logger.warning("Invalid state. Discarding")
			return False

		if not 'file_name' in message:
			logger.warning("No filename in Open")
			return False

		# Only chars and letters in the filename
		file_name = re.sub(r'[^\w\.]', '', message['file_name'])
		file_path = os.path.join(self.storage_dir, file_name)
		if not os.path.exists("files"):
			try:
				os.mkdir("files")
			except:
				logger.exception("Unable to create storage directory")
				return False

		try:
			self.file = open(file_path, "wb")
			logger.info("File open")
		except Exception:
			logger.exception("Unable to open file")
			return False

		self._send({'type': 'OK'})

		self.file_name = file_name
		self.file_path = file_path
		self.state = STATE_OPEN
		return True


	def process_data(self, message: str) -> bool:
		"""
		Processes a DATA message from the client
		This message should contain a chunk of the file

		:param message: The message to process
		:return: Boolean indicating the success of the operation
		"""
		logger.debug("Process Data: {}".format(message))

		if self.state == STATE_OPEN:
			self.state = STATE_DATA
			# First Packet

		elif self.state == STATE_DATA:
			# Next packets
			pass

		else:
			logger.warning("Invalid state. Discarding")
			return False

		try:
			data = message.get('data', None)
			if data is None:
				logger.debug("Invalid message. No data found")
				return False

			bdata = base64.b64decode(message['data'])
		except:
			logger.exception("Could not decode base64 content from message.data")
			return False

		try:
			self.file.write(bdata)
			self.file.flush()
		except:
			logger.exception("Could not write to file")
			return False

		return True


	def process_close(self, message: str) -> bool:
		"""
		Processes a CLOSE message from the client.
		This message will trigger the termination of this session

		:param message: The message to process
		:return: Boolean indicating the success of the operation
		"""
		logger.debug("Process Close: {}".format(message))

		self.transport.close()
		if self.file is not None:
			self.file.close()
			self.file = None

		self.state = STATE_CLOSE

		return True


	def _send(self, message: str) -> None:
		"""
		Effectively encodes and sends a message
		:param message:
		:return:
		"""
		logger.debug("Send: {}".format(message))

		message_b = (json.dumps(message) + '\r\n').encode()
		self.transport.write(message_b)

	#######################################
	# Criar users e suas passwords
	def user(self):
		letters_digits = string.ascii_letters + string.digits  # nao inclui " "
		return ''.join(random.choice(letters_digits) for i in range(int(random.random() * 7 + 3)))

	def password(self):
		password_characters = string.ascii_letters + string.digits + string.punctuation  # tmb nao inclui " "
		return ''.join(random.choice(password_characters) for i in range(int(random.random() * 15 + 5)))

	def generate_file(self):
		file = open('users.txt', 'w')
		for data in range(int(random.random() * 999 + 1)):
			file.write(str(user()) + '\n')
			file.write(str(password()) + '\n')
		file.close()

	#######################################################
	#Sending Password Challenge
	def processUser(self, message: str):
		lista_ficheiro =open('users.txt', 'r')
		users = [u for u in lista_ficheiro if u%2 == 0]
		passwords = [p for p in lista_ficheiro if p%2 == 0]
		if message['username'] in users:
			self.user = message['username']
			self.password = passwords[ ((users.index(message['username'])+1))+1]
			self._send({'type': 'CHALLENGE', 'challenge': 'PASSWORD'})
			return True
		else:
			print("Failed to process User/Password")
			return False



	#######################################################
	#Processing message Challenge from client, if equal OK if not close the communication
	def processChallenge(self,message: str) -> bool:
		if message['answer'] == self.password:
			return True
		print("Failed Challenge-Answer")
		return False

	#######################################################
	#CC Authentication
	def cc_function(self):
		self.private_key = rsa.generate_private_key(
			public_exponent=65537,
			key_size=2048,
			backend=default_backend())
		csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
			# Provide various details about who we are.
			x509.NameAttribute(NameOID.COUNTRY_NAME, u"PT"),
			x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"AVEIRO"),
			x509.NameAttribute(NameOID.LOCALITY_NAME, u"AVEIRO"),
			x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UA"),
			x509.NameAttribute(NameOID.COMMON_NAME, u"Server"),
		])).add_extension(
			x509.SubjectAlternativeName([
				# Describe what sites we want this certificate for.
				x509.DNSName(u"mysite.com"),
				x509.DNSName(u"www.mysite.com"),
				x509.DNSName(u"subdomain.mysite.com"),
			]),
			critical=False,
			# Sign the CSR with our private key.
		).sign(self.private_key, hashes.SHA256(), default_backend())

		self._send({'type': 'CC', 'certificate': csr})

	#######################################################
	#Process response from client for CC Authentication
	def process_cc_authentication(self,message):
		return False

	#######################################################
	#Create and send certificate to be authenticated by client
	def create_certificate(self):
		self.private_key = rsa.generate_private_key(
			public_exponent=65537,
			key_size=2048,
			backend=default_backend())
		csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
			# Provide various details about who we are.
				x509.NameAttribute(NameOID.COUNTRY_NAME, u"PT"),
			    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"AVEIRO"),
				x509.NameAttribute(NameOID.LOCALITY_NAME, u"AVEIRO"),
			    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UA"),
				x509.NameAttribute(NameOID.COMMON_NAME, u"Server"),
			])).add_extension(
		x509.SubjectAlternativeName([
			# Describe what sites we want this certificate for.
				x509.DNSName(u"mysite.com"),
			    x509.DNSName(u"www.mysite.com"),
			    x509.DNSName(u"subdomain.mysite.com"),
			]),
		critical = False,
				# Sign the CSR with our private key.
				).sign(self.private_key, hashes.SHA256(), default_backend())

		self.send({'type': 'CERTIFICATE', 'certificate': csr})

	#######################################################
	#Process response from client for certifiicate authentication
	def process_certificate(self, message):
		return False

def main():
	global storage_dir

	parser = argparse.ArgumentParser(description='Receives files from clients.')
	parser.add_argument('-v', action='count', dest='verbose',
						help='Shows debug messages (default=False)',
						default=0)
	parser.add_argument('-p', type=int, nargs=1,
						dest='port', default=5000,
						help='TCP Port to use (default=5000)')

	parser.add_argument('-d', type=str, required=False, dest='storage_dir',
						default='files',
						help='Where to store files (default=./files)')

	args = parser.parse_args()
	storage_dir = os.path.abspath(args.storage_dir)
	level = logging.DEBUG if args.verbose > 0 else logging.INFO
	port = args.port
	if port <= 0 or port > 65535:
		logger.error("Invalid port")
		return

	if port < 1024 and not os.geteuid() == 0:
		logger.error("Ports below 1024 require eUID=0 (root)")
		return

	coloredlogs.install(level)
	logger.setLevel(level)

	logger.info("Port: {} LogLevel: {} Storage: {}".format(port, level, storage_dir))
	tcp_server(ClientHandler, worker=2, port=port, reuse_port=True)


if __name__ == '__main__':
	main()


