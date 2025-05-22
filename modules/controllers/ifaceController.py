import modules.parsers.ifaceParser as ifaceParser 
from modules.ui.debug import info, success
from modules.consts import UP, DOWN


class ifaceController:
	def __init__(self, session) -> None:
		self.session = session
		pass

	def get_brief(self, router: str):
		parsed = ifaceParser.parse_brief(
			self.session.send_command("sh ip int br")
		)
		
		return parsed


	def get_iface(self, iface: str):
		result = self.session.send_command(f"sh ip int {iface}")
		return result


	def toggle(self, iface: str):
		info(f"Determining wether {iface} is {UP} or {DOWN}")

		result = self.get_iface_controller(iface)
		state = "is up" in result

		success(f"Interface {iface} is {UP if state else DOWN}")

		cfg_set = [
			f"interface {iface}",
			"no sh" if(state) else "sh"
		]

		self.session.enable()
		return self.session.send_config_set(cfg_set)