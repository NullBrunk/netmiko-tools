from modules.parser.interfaces import display_brief
from modules.consts import USERNAME, PASSWORD, UP, DOWN
from modules.ui.debug import info, success
from netmiko import ConnectHandler
from termcolor import colored

def show(router: str):
	net_connect = ConnectHandler(device_type="cisco_ios", host=router, username=USERNAME, password=PASSWORD)
	result = display_brief(net_connect.send_command("sh ip int br"))

	return net_connect, result


def toggle(router: str, iface: str) -> None:
	info(f"Determining wether {iface} is {UP} or {DOWN}")
	
	net_connect, res = show(router, iface)
	state = "is up" in res

	success(f"Interface {iface} is {UP if state else DOWN}")

	cfg_set = [
		f"interface {iface}",
		"no sh" if(state) else "sh"
	]

	net_connect.enable()
	print(net_connect.send_config_set(cfg_set))