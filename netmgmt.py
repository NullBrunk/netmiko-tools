#!/usr/bin/env python3

from modules.interfaces import get_info as show_interfaces, toggle as toggle_interfaces
from modules.debug import success, info, error, presentation
from modules.ui.date_calculator import date_calculator

from termcolor import colored
from modules.consts import ROUTERS, ROUTERS_STRING
from time import strftime
import argparse

start = strftime("%H:%M:%S")

def main(args):
    hostname = args.hostname
    backup = args.backup
    show_all = args.show_all
    interface = args.interface
    toggle = args.toggle

    # Vérifier que le hostname existe
    if(hostname not in ROUTERS):
        error(f"{hostname} is not a valid hostname")
        info(f"Please choose a router in: {ROUTERS_STRING}")
        quit()
    ip = ROUTERS[hostname]
    
    if(backup):
        backup()

    elif(show_all):
        info(f'Executing "{colored("sh ip int br", "white", attrs=["bold"])} on "{colored(hostname, "white", attrs=["bold"])}"\n')
        res = show_interfaces(router=ip, iface="")
        print(res[1])

    elif(interface != None):
        if(toggle):
            res = toggle_interfaces(router=ip, iface=interface)
            print(res[1])

        else:
            success(f'Executing "{colored(f"sh ip int {interface}", "white", attrs=["bold"])} on "{colored(hostname, "white", attrs=["bold"])}"\n')
            res = show_interfaces(router=ip, iface=interface)
            print(res[1])
    
    else:
        error("Nothing to do !")


    info(f'Ending script at {colored(strftime("%H:%M:%S"), "white", attrs=["bold"])} took {colored(date_calculator(start, strftime("%H:%M:%S")), "white", attrs=["bold"])}', start="\n")
    
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cisco network management script")
    parser.add_argument("hostname", help="The router which you want to configure")
    parser.add_argument("-b", "--backup", help="Backup the running config", action="store_true", required=False)
    parser.add_argument("-sa", "--show-all", help="Send sh ip int br to the router", action="store_true", required=False)
    parser.add_argument("-i", "--interface", help="The interface which you want to configure", required=False)
    parser.add_argument("-t", "--toggle", help="Toggle the state of an interface", action="store_true", required=False)

    args = parser.parse_args()
    main(args)