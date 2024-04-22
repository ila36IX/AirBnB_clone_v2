#!/usr/bin/python3
"""
Deletes out-of-date archives,
"""
from fabric.api import *
from datetime import datetime
import os.path

# env.hosts = [
#     "18.206.208.23",
#     "54.210.152.224"
# ]

def do_clean(number):
    """Deletes out-of-date archives,
    - number: is the number of the archives to keep.
    
    Usage:
        fab -f script_file do_clean
    """
    list_archives = local("ls -1vr versions/web_static*", capture=True)
    for archive in list_archives.split("\n")[:int(number)]:
        print("rm -rf {}".format(archive))
