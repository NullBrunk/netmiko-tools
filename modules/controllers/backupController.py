from os.path import abspath
from os import makedirs

from time import strftime

from modules.ui.logger import log

class backupController:
    def __init__(self, session) -> None:
        self.session = session
        
    def do_backup(self):
        self.session.enable()

        startup_config = self.session.send_command(f"sh startup")
        running_config = self.session.send_command(f"sh run")

        # On génére un nom unique basé sur Année Mois Jour Heure Minute Secondes

        backup_folder = abspath(__file__ + "../backups/") + strftime("%Y-%m-%d_%H-%M-%S")
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
        