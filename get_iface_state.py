#!/usr/bin/env python3

from netmiko import ConnectHandler
from termcolor import colored
from sys import argv

DNS = {"PE1": "10.50.50.252", "PE2": "10.50.50.253", "PE3": "10.3.3.1", "P1": "10.99.99.2", "P2": "10.99.99.14"}
USERNAME = "aaa_user"
PASSWORD = "root"

def main(hostname: str, iface: str) -> None:

	router_ip = DNS[hostname.upper()]

	# Ternary pour executer "sh ip int br" si aucune interface a été passée en CLI, sh ip int <l'interface> sinon
	command = "sh ip int " + ( iface if(iface) else "br" )

	print(f"{colored('[*]', 'cyan')} Executing \"{command}\" on {hostname}\n")

	# On se co en SSH en utilisant les creds RADIUS
	net_connect = ConnectHandler(device_type="cisco_ios", host=router_ip, username=USERNAME, password=PASSWORD)

	# On envoie la commande et on log le retour
	print(net_connect.send_command(command))


if __name__ == "__main__":
	if(len(argv) == 1):
		print(f"{colored('[!]', 'red')} Missing mandatory argument: HOSTNAME")
		print(f"{colored('[*]', 'cyan')} Usage: {argv[0]} (HOSTNAME) [IFACE]\n")
		quit()

	if(argv[1] in ["-h", "--help", "help", "h"]):
		print(f"{colored('[*]', 'cyan')} Usage: {argv[0]} (HOSTNAME) [IFACE]")
		print(f"{colored('[i]', 'green')} Example: {argv[0]} PE1")
		print(f"             {argv[0]} PE2 e0/0 \n")
		quit()

	iface = ""
	if(len(argv) >= 3):
		iface = argv[2]

	main(argv[1], iface)
