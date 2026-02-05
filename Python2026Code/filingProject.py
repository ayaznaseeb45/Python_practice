import os


USER_FILE = "users.txt"
LOG_FILE = "activity.log"
BACKUP_FILE = "activity_backup.log"
SUMMARY_FILE = "summary"


def backup():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as srcFile:
            data = srcFile.read()
        with open(BACKUP_FILE, "w") as backupFile:
            backupFile.write(data)
