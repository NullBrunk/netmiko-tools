from modules.ui.logger import log
from termcolor import colored

def dataframe(df):
    # On recupere les interfaces qui ont une ip
    up_interfaces = df[df["status"] == "up"]
    # On recupere les interfaces qui ont pas d'ip
    down_interfaces = df[df["status"] == "down"]


    # On affiche les interfaces qui ont une IP sort by le fait qu'elle soit up ou down
    log.presentation(f"{colored('UP', 'green', attrs=['bold'])}", "interfaces")
    print(up_interfaces, end="\n\n")

    # On affiche les interfaces qui ont pas d'IP sort by le fait qu'elle soit up ou down
    log.presentation(f"{colored('DOWN', 'red', attrs=['bold'])}", "interfaces")
    print(down_interfaces)


    total = len(df)
    up_count = (df["status"] == "up").sum()
    down_count = (df["status"] == "down").sum()

    print(f"\n\n{colored(f'{total} interfaces', 'white', attrs=['bold'])} ({colored(up_count, 'white', attrs=['bold'])} {colored('UP', 'green', attrs=['bold'])}, {colored(down_count, 'white', attrs=['bold'])} {colored('DOWN', 'red', attrs=['bold'])})")
    

def iface(res):
    print(res)