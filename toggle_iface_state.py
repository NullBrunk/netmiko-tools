#!/usr/bin/env python3

from netmiko import ConnectHandler
from termcolor import colored
from sys import argv

ROUTERS = {"PE1": "10.50.50.252", "PE2": "10.50.50.253", "PE3": "10.3.3.1"}
USERNAME = "aaa_user"
PASSWORD = "root"

def main(hostname: str, iface: str, state: str) -> None:

	router_ip = ROUTERS[hostname.upper()]
	cfg_set = [
		f"interface {iface}",
		"no sh" if(state == "on") else "sh"
	]

	print(f"{colored('[*]', 'cyan')} Switching {state} {iface} on {hostname}\n")

	# On se co en SSH en utilisant les creds RADIUS
	net_connect = ConnectHandler(device_type="cisco_ios", host=router_ip, username=USERNAME, password=PASSWORD)


	# Pour envoyer des confs il faut d'abord passer en enable
	net_connect.enable()
	print(net_connect.send_config_set(cfg_set))


if __name__ == "__main__":
	if(argv[1] and argv[1] in ["-h", "--help", "help", "h"]):
		print(f"{colored('[*]', 'cyan')} Usage: {argv[0]} (HOSTNAME) (IFACE) (on|off)")
		print(f"{colored('[i]', 'green')} Example: {argv[0]} PE1 e0/0 off")
		quit()


	if(len(argv) < 4):
		print(f"{colored('[!]', 'red')} Usage: {argv[0]} (HOSTNAME) (IFACE) (on|off)\n")
		quit()

	main(argv[1], argv[2], argv[3])
