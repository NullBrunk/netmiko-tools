#!/usr/bin/env python3

from modules.controllers.ifaceController import ifaceController
from modules.controllers.backupController import backupController
from modules.controllers.routeController import routeController

import modules.ui.interfaces as ui_interfaces
import modules.ui.routes as ui_routes
import modules.ui.backup as ui_backup


from modules.ui.dateui import date_calculator
from modules.ui.logger import log

from netmiko import ConnectHandler


from termcolor import colored
from modules.consts import ROUTERS, ROUTERS_STRING, USERNAME, PASSWORD
from time import strftime
import argparse


start = strftime("%H:%M:%S")

def main(args):
    hostname = args.hostname

    # Vérifier que le hostname existe
    if(hostname not in ROUTERS):
        log.error(f"{hostname} is not a valid hostname")
        log.info(f"Please choose a router in: {ROUTERS_STRING}")
        quit()

    ip = ROUTERS[hostname]
    session = ConnectHandler(device_type="cisco_ios", host=ip, username=USERNAME, password=PASSWORD, fast_cli=True,)

    if(args.component == "ifaces"):
        ic = ifaceController(session=session)

        if(args.list_all):
            ui_interfaces.dataframe(ic.get_brief())
        elif(args.list and args.interface != None):
            ui_interfaces.iface(ic.get_iface(iface=args.interface))
        elif(args.toggle and args.interface != None):
            ui_interfaces.iface(ic.toggle(iface=args.interface))
        else:
            log.error("nothing to do")

    elif(args.component == "routes"):
        rc = routeController(session=session, vrf=args.vrf)
        
        if(args.list_all):
            ui_routes.show(rc.all())
        elif(args.ospf):
            ui_routes.show(rc.ospf())
        elif(args.bgp):
            ui_routes.show(rc.bgp())
        elif(args.static):
            ui_routes.show(rc.static())
        else:
            log.error("nothing to do")

    elif(args.component == "backups"):
        bc = backupController(hostname=hostname, session=session)

        if(args.make):
            bc.make()
        elif(args.list_all):
            bc.list_backups()
        else:
            log.error("nothing to do")


    log.info(f'Took {colored(date_calculator(start, strftime("%H:%M:%S")), "white", attrs=["bold"])}', start="\n")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cisco network management script")
    parser.add_argument("hostname", help="The router which you want to configure")

    subparsers = parser.add_subparsers(dest="component", required=True)

    # ./netmgmt.py PE1 ifaces ......
    interface_parser = subparsers.add_parser("interfaces", help="Manage interfaces")
    interface_parser.add_argument("-i", "--interface",  help="Specify an interface")
    interface_parser.add_argument("-l", "--list", action="store_true", help="Show the interface")
    interface_parser.add_argument("-la", "--list-all", action="store_true", help="Show all the interfaces")
    interface_parser.add_argument("-t", "--toggle", help="Toggle the state", action="store_true", required=False)

    # ./netmgmt.py PE1 routes ......
    router_parser = subparsers.add_parser("routes", help="Manage routes")
    router_parser.add_argument("-v", "--vrf", help="Specify a VRF")
    router_parser.add_argument("-la", "--list-all", action="store_true", help="Show routes")
    router_parser.add_argument("-o", "--ospf", action="store_true", help="Show OSPF routes")
    router_parser.add_argument("-b", "--bgp", action="store_true", help="Show BGP routes")
    router_parser.add_argument("-s", "--static", action="store_true", help="Show static routes")
    
    # ./netmgmt.py PE1 backups ......
    backup_parser = subparsers.add_parser("backups", help="Manage backups")
    backup_parser = backup_parser.add_mutually_exclusive_group(required=True)
    backup_parser.add_argument("-m", "--make", help="Make a backup", action="store_true", required=False)
    backup_parser.add_argument("-la", "--list-all", help="List all backups", action="store_true", required=False)


    args = parser.parse_args()
    main(args)