#!/usr/bin/env python3

import datetime
import tarfile
import os
import subprocess as cmd

date = datetime.datetime.now().strftime("%Y-%m-%d")

#############"" CONFIGURATION #############
#########################################

backup_folder = ["/data/VPN", "/data/cheatsheet"]
bucket = "backup-noxas"
retention = 5

##########################################
##########################################

def backup():
    with tarfile.open(f"/tmp/backup-{date}.tar.gz", mode="w:gz") as archive:
        for folder in backup_folder:
            archive.add(folder)


    cmd.run(f"s3cmd put -r /tmp/backup-{date}.tar.gz s3://{bucket}", shell=True)
    os.remove(f"/tmp/backup-{date}.tar.gz")


def check_retention():
    proc = cmd.Popen([f"s3cmd ls s3://{bucket}"], stdout=cmd.PIPE, stdin=cmd.PIPE, shell=True)
    out = proc.stdout.readlines()
    count = len(out)

    if count >= retention:
        d = datetime.datetime.today() - datetime.timedelta(days=1)
        date2 = d.strftime("%Y-%m-%d")
        cmd.run(f"s3cmd del s3://{bucket}/backup-{date2}.tar.gz", shell=True)

  

check_retention()
backup()
