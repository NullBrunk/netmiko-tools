from termcolor import colored

ROUTERS = {}


with open("dns.txt", "r") as dns_file:
    dns_file = dns_file.read().strip().split("\n")

for line in dns_file:
    if line.startswith("#"):
        continue
    if line.strip() == "":
        continue

    splited_line = line.split(" ")
    ROUTERS[splited_line[0]] = splited_line[1]

ROUTERS_STRING = ", ".join([router for router in ROUTERS])
ROUTERS_PROMPT = ROUTERS_STRING.replace(" ", "")
USERNAME = "aaa_user"
PASSWORD = "root"
UP = colored("UP", "green", attrs=["bold"])
DOWN = colored("DOWN", "red", attrs=["bold"])