from modules.parser.parse_interfaces import parse_interface_brief
from modules.consts import USERNAME, PASSWORD
from netmiko import ConnectHandler
from modules.ui.debug import info, success
from termcolor import colored

def get_info(router: str, iface: str):

	# executer "sh ip int br" si aucune interface a été passée en CLI, 
	# sinon executer sh ip int <l'interface>
	command = "sh ip int " + ( iface if(iface) else "br" )

	# On se co en SSH en utilisant les creds RADIUS
	net_connect = ConnectHandler(device_type="cisco_ios", host=router, username=USERNAME, password=PASSWORD)
	result = net_connect.send_command(command)

	result = parse_interface_brief()
	return net_connect, result


def toggle(router: str, iface: str) -> None:
	green_up = colored("UP", "green", attrs=["bold"])
	red_down = colored("DOWN", "red", attrs=["bold"])

	info(f"Determining wether {iface} is {green_up} or {red_down}")
	
	# Determine if the interface is up, or down
	net_connect, res = get_info(router, iface)
	state = "is up" in res

	success(f"Interface {iface} is {green_up if state else red_down}")

	cfg_set = [
		f"interface {iface}",
		"no sh" if(state) else "sh"
	]

	# Pour envoyer des confs il faut d'abord passer en enable
	net_connect.enable()
	print(net_connect.send_config_set(cfg_set))

