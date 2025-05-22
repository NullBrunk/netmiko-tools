from termcolor import colored

ROUTERS = {"PE1": "10.50.50.252", "PE2": "10.50.50.253", "PE3": "10.3.3.1"}
ROUTERS_STRING = ", ".join([router for router in ROUTERS])
ROUTERS_PROMPT = ROUTERS_STRING.replace(" ", "")
USERNAME = "aaa_user"
PASSWORD = "root"
UP = colored("UP", "green", attrs=["bold"])
DOWN = colored("DOWN", "red", attrs=["bold"])