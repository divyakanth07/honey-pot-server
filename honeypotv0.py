import socket 
import logging
from datetime import datetime

logging.basicConfig(filename="honeypotpie.log", level=logging.INFO, format='%(asctime)s %(message)s')

host = '127.0.0.1'
port = 4545
def start_honeypot(host, port):
	server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen(5)
	print(f'[+] HoneyPotPie is being serverd on {host}: {port}')

	while True:
		client_socket , client_address = server_socket.accept()
		print(f'[-] Connection from {client_address}')

		logging.info(f'Connection from {client_address}')

		client_socket.send(b'Kali GNU/Linux Rolling\n')

		client_socket.close()

if __name__ == '__main__':
	start_honeypot(host, port)