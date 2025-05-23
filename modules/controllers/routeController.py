class routeController:
    def __init__(self, session, vrf: str) -> None:
        self.session = session

        self.to_add = ""
        if(vrf != None):
            self.to_add = f"vrf {vrf}"

    def all(self):
        result = self.session.send_command(f"sh ip route {self.to_add} | include /")
        return result
    
    def ospf(self):
        result = self.session.send_command(f"sh ip route {self.to_add} ospf | include /")
        return result

    def bgp(self):
        result = self.session.send_command(f"sh ip route {self.to_add} bgp | include /")
        return result
    
    def static(self):
        result = self.session.send_command(f"sh ip route {self.to_add} static | include /")
        return result
