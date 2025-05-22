from modules.ui.debug import presentation
from termcolor import colored

def display_interfaces_dataframe(df):
    # On recupere les interfaces qui ont une ip
    ip_interfaces = df[df["address"] != "unassigned"]
    # On recupere les interfaces qui ont pas d'ip
    noip_interfaces = df[df["address"] == "unassigned"]

    status_order = {'up': 0, 'down': 1}
    with_ip_sorted = ip_interfaces.assign(status_order=ip_interfaces["status"].map(status_order)) \
        .sort_values("status_order") \
        .drop(columns="status_order")

    without_ip_sorted = noip_interfaces.assign(status_order=noip_interfaces["status"].map(status_order)) \
        .sort_values("status_order") \
        .drop(columns="status_order")

    # On affiche les interfaces qui ont une IP sort by le fait qu'elle soit up ou down
    presentation(f"> {colored('UP', 'green', attrs=['bold'])} interfaces")
    print(with_ip_sorted)

    # On affiche les interfaces qui ont pas d'IP sort by le fait qu'elle soit up ou down
    presentation(f"> {colored('DOWN', 'red', attrs=['bold'])} interfaces")
    print(without_ip_sorted)


    total = len(df)
    up_count = (df["status"] == "up").sum()
    down_count = (df["status"] == "down").sum()

    print(f"> {total} interfaces ({up_count} {colored('UP', 'green', attrs=['bold'])}, {down_count} {colored('DOWN', 'red', attrs=['bold'])})")
    
