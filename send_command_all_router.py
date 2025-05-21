#!/usr/bin/env python3

from netmiko import ConnectHandler
from termcolor import colored

USERNAME: str = "aaa_user"
PASSWORD: str = "root"

ROUTERS: dict = {"PE1": "10.50.50.252", "PE2": "10.50.50.253", "PE3": "10.3.3.1"} 
ROUTERS_JOINED: str = ",".join(router for router in ROUTERS)

PROMPT: str = f"""{colored("ROUTERS(", "white", attrs=["bold"])}{ROUTERS_JOINED}{colored(")", "white", attrs=["bold"])}# """
SESSIONS: dict = {}

def configure() -> None:
	print("Not available")

def get_result() -> None:
	while True:
		command = input(PROMPT)
		if command in ["exit", "quit", "end", "next"]:
			return
		
		if(command.strip() == ""):
			continue
		
		for router in SESSIONS:
			print(colored(f"> {router}", "cyan", attrs=["bold"]))
			session = SESSIONS[router]
			res = session.send_command(command)
			print(res)
		
def main() -> None:
	while True:
		print(f"""
{colored("What do you want to do ?", "white", attrs=["bold"])}
{colored("1>", "cyan", attrs=["bold"])} {colored("Send configs", "white")}
{colored("2>", "cyan", attrs=["bold"])} {colored("Get command result", "white")}

> """, end="")

		try:
			todo: str = input()
		except:
			print(f"\n{colored('[!]', 'yellow', attrs=['bold'])} Received SIGKILL, exiting ...")
			quit()
		try:
			todo: int = int(todo)
		except:
			continue

		if(todo == 1):
			configure()
		elif(todo == 2):
			get_result()
		else:
			continue

if __name__ == "__main__":
	print(f"""{colored("[*]", "cyan", attrs=["bold"])} Initializing SSH session for {ROUTERS_JOINED}""")
	for router in ROUTERS:
		SESSIONS[router] = ConnectHandler(device_type="cisco_ios", host=ROUTERS[router], username=USERNAME, password=PASSWORD)
	print(f"""{colored("[+]", "green", attrs=["bold"])} Done""")

	main()