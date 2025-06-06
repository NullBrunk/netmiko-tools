import modules.parsers.ifaceParser as ifaceParser 
from modules.ui.logger import log
from modules.consts import UP, DOWN


class ifaceController:
	def __init__(self, session) -> None:
		self.session = session

	def get_brief(self):
		parsed = ifaceParser.parse_brief(
			self.session.send_command("sh ip int br")
		)
		
		return parsed


	def get_iface(self, iface: str):
		result = self.session.send_command(f"sh ip int {iface}")
		return result


	def toggle(self, iface: str):
		log.info(f"Determining wether {iface} is {UP} or {DOWN}")

		result = self.get_iface(iface)
		state = "is up" in result

		log.success(f"Interface {iface} is {UP if state else DOWN}")

		cfg_set = [
			f"interface {iface}",
			"sh" if(state) else "no sh"
		]

		self.session.enable()
		return self.session.send_config_set(cfg_set)