#!/usr/bin/env python3

from netmiko import ConnectHandler
from termcolor import colored

USERNAME = "aaa_user"
PASSWORD = "root"
													      # Le SSH vers PE3, P1 et P2 marche plus donc pour l'instant ils sont punis ...	
ROUTERS = {"PE1": "10.50.50.252", "PE2": "10.50.50.253",} # "PE3": "10.3.3.1", "P1": "10.99.99.2", "P2": "10.99.99.14"}
ROUTERS_JOINED = ",".join(router for router in ROUTERS)

PROMPT = f"""{colored("ROUTERS(", "white", attrs=["bold"])}{ROUTERS_JOINED}{colored(")", "white", attrs=["bold"])}# """
SESSIONS = {}


def configure():
	# on verra un de ces 4
	return

def get_result():
	while True:
		command = input(PROMPT)
		if command in ["exit", "quit", "end", "next"]:
			return
		
		for router in SESSIONS:
			print(colored(f"> {router}", "cyan", attrs=["bold"]))
			session = SESSIONS[router]
			res = session.send_command(command)
			print(res)

def main():
	while True:
		print(f"""
{colored("What do you want to do ?", "white", attrs=["bold"])}
{colored("1>", "cyan", attrs=["bold"])} {colored("Send configs", "white")}
{colored("2>", "cyan", attrs=["bold"])} {colored("Get command result", "white")}

> """, end="")

		todo = input()

		try:
			todo = int(todo)
		except:
			continue

		if(todo == 1):
			configure()
		elif(todo == 2):
			get_result()
		else:
			continue

if __name__ == "__main__":
	print(f"{colored("[*]", "cyan", attrs=["bold"])} Initializing SSH session for all {ROUTERS_JOINED}")
	for router in ROUTERS:
		SESSIONS[router] = ConnectHandler(device_type="cisco_ios", host=ROUTERS[router], username=USERNAME, password=PASSWORD)
	print(f"{colored("[+]", "green", attrs=["bold"])} Done")

	main()