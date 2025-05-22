def get_info(router: str, iface: str) -> None:

	# executer "sh ip int br" si aucune interface a été passée en CLI, 
	# sinon executer sh ip int <l'interface>
	command = "sh ip int " + ( iface if(iface) else "br" )

	# On se co en SSH en utilisant les creds RADIUS
	net_connect = ConnectHandler(device_type="cisco_ios", host=router, username=USERNAME, password=PASSWORD)

	# TODO: Parse with **pandas** by Interface, IP, Status and protocol columns
	print(net_connect.send_command(command))
	# TODO: Make resume, alerts etc ... improve UX


def toggle(router: str, iface: str, state: str) -> None:

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

