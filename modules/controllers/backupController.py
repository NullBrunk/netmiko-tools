from os.path import abspath, dirname
from os import makedirs, listdir

from time import strftime

from modules.ui.logger import log

class backupController:
    def __init__(self, hostname: str, session) -> None:
        self.hostname = hostname
        self.session = session
        self.convertion = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        
    def make(self):
        self.session.enable()

        startup_config = self.session.send_command(f"sh startup")
        running_config = self.session.send_command(f"sh run")

        # On génére un nom unique basé sur Année Mois Jour Heure Minute Secondes

        backup_folder = abspath(dirname(__file__) + "/../../backups/") + "/" + self.hostname + "_" + strftime("%Y-%m-%d_%H-%M-%S")
        makedirs(backup_folder, exist_ok=True)

        startup_config_backup = backup_folder + "/startup_config"
        running_config_backup = backup_folder + "/running_config"

        log.info(f"Backing up startup config in {startup_config_backup}")
        with open(startup_config_backup, "w") as f:
            f.write(startup_config)

        log.info(f"Backing up startup config in {running_config_backup}")
        with open(running_config_backup, "w") as f:
            f.write(running_config)

        log.success("Done")

    def list_backups(self):
        backups = listdir("backups")

        # Ce dict sera du genre {
        # "PE1": ["PE1_2025-05-23_02-03-09", "PE1_2025-05-23_02-03-12"]
        # "PE2": ["PE2_2025-05-23_02-04-21", "PE2_2025-05-23_02-06-09"]
        #}
        backed_up_routers = {}
        for backup in backups:
            hostname = backup.split("_")[0]

            if(not hostname in backed_up_routers):
                backed_up_routers[hostname] = []
                
            backed_up_routers[hostname].append(backup)

        # On trie les clés histoire que ca soit plus propre
        backed_up_routers = dict(sorted(backed_up_routers.items()))

        for router in backed_up_routers:
            log.presentation(router, "")
            backups = backed_up_routers[router]
            backups.sort()

            for backup in backups:
                path = abspath(dirname(__file__) + "/../../backups/") + "/" + backup

                backup = backup.split("_")
                date = backup[1].split("/")
                hour = ':'.join(backup[2].split("-")[:2])

                date = f"{int(date[1])-1} {date[2]}, {date[0]} at {hour}"


                print(date, "    ", path)