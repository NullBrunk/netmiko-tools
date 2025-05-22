#!/usr/bin/env python3

from modules.controllers.ifaceController import ifaceController

from modules.ui.debug import success, info, error, presentation
import modules.ui.interfaces as ui_interfaces
from modules.ui.datetime import date_calculator

from netmiko import ConnectHandler


from termcolor import colored
from modules.consts import ROUTERS, ROUTERS_STRING, USERNAME, PASSWORD
from time import strftime
import argparse


start = strftime("%H:%M:%S")

def main(args):
    hostname = args.hostname
    backup = args.backup
    show_interface = args.show_interfaces
    interface = args.interface
    toggle = args.toggle

    # Vérifier que le hostname existe
    if(hostname not in ROUTERS):
        error(f"{hostname} is not a valid hostname")
        info(f"Please choose a router in: {ROUTERS_STRING}")
        quit()

    ip = ROUTERS[hostname]
    session = ConnectHandler(device_type="cisco_ios", host=ip, username=USERNAME, password=PASSWORD)

    ic = ifaceController(session=session)

    if(backup):
        backup()

    # L'utilisateur veut afficher TOUTES les interfaces du routeur
    elif(show_interface):
        success(f'Executing "{colored(f"sh ip int br", "white", attrs=["bold"])} on "{colored(hostname, "white", attrs=["bold"])}"\n')

        ui_interfaces.dataframe(
            ic.get_brief()
        )


    elif(interface != None):
        if(toggle):
            ui_interfaces.iface(
                ic.toggle(iface=interface)
            )

        else:
            success(f'Executing "{colored(f"sh ip int {interface}", "white", attrs=["bold"])} on "{colored(hostname, "white", attrs=["bold"])}"\n')
            ui_interfaces.iface(
                ic.get_iface(iface=interface)
            )
    
    else:
        error("Nothing to do !")


    info(f'Took {colored(date_calculator(start, strftime("%H:%M:%S")), "white", attrs=["bold"])}', start="\n")
    
    

if __name__ == "__main__":

    print("Je commence")
    parser = argparse.ArgumentParser(description="Cisco network management script")
    parser.add_argument("hostname", help="The router which you want to configure")
    parser.add_argument("-b", "--backup", help="Backup the running config", action="store_true", required=False)
    parser.add_argument("-si", "--show-interfaces", help="Send sh ip int br to the router", action="store_true", required=False)
    parser.add_argument("-i", "--interface", help="The interface which you want to configure", required=False)
    parser.add_argument("-t", "--toggle", help="Toggle the state of an interface", action="store_true", required=False)
    print("Middle")

    args = parser.parse_args()
    print("Go main")
    main(args)