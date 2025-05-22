#!/usr/bin/env python3

from netmiko import ConnectHandler
from termcolor import colored
from sys import argv

ROUTERS = {"PE1": "10.50.50.252", "PE2": "10.50.50.253", "PE3": "10.3.3.1"}
USERNAME = "aaa_user"
PASSWORD = "root"

def main(hostname: str, iface: str) -> None:

	router_ip = ROUTERS[hostname.upper()]

	# executer "sh ip int br" si aucune interface a été passée en CLI, 
	# sinon executer sh ip int <l'interface>
	command = "sh ip int " + ( iface if(iface) else "br" )

	print(f"{colored('[*]', 'cyan')} Executing \"{command}\" on {hostname}\n")

	# On se co en SSH en utilisant les creds RADIUS
	net_connect = ConnectHandler(device_type="cisco_ios", host=router_ip, username=USERNAME, password=PASSWORD)

	# TODO: Parse with **pandas** by Interface, IP, Status and protocol columns
	print(net_connect.send_command(command))
	# TODO: Make resume, alerts etc ... improve UX


def _help() -> None:
	print(f"{colored('[*]', 'cyan')} Usage: {argv[0]} (HOSTNAME) [IFACE]\n")

if __name__ == "__main__":
	if(len(argv) == 1):
		print(f"{colored('[!]', 'red')} Missing mandatory argument: HOSTNAME")
		_help()
		quit()

	if(argv[1] in ["-h", "--help", "help", "h"]):
		_help()
		print(f"{colored('[i]', 'green')} Example: {argv[0]} PE1")
		print(f"             {argv[0]} PE2 e0/0 \n")
		quit()

	iface = ""
	if(len(argv) >= 3):
		iface = argv[2]

	main(argv[1], iface)
