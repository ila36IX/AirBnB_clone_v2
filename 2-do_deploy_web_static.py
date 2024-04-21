#!/usr/bin/python3
"""
Distributes an archive to your web servers
"""
from fabric.api import *
from datetime import datetime
import os.path

env.user = "ubuntu"
env.hosts = [
    "18.206.208.23",
    "54.210.152.224"
]


def do_deploy(archive_path):
    """Distributes an archive to your web servers
        Usage:
            fab -f 2-do_deploy_web_static.py
            do_deploy:<path/to/archive>
            [-i my_ssh_private_key -u ubuntu]
    """
    if not os.path.isfile(archive_path):
        return False
    # Upload the archive to the /tmp/ directory of the web server
    cmd1 = put(archive_path, "/tmp/")

    releases_path = "/data/web_static/releases/"
    # Get the name of the archive web_static_longdate.org
    archive_file = archive_path.split("/")[-1]
    # The path where archive is located in the curr remote server
    remote_archive_path = "/tmp/" + archive_file
    # The path where archive will be extracted
    new_release_path = releases_path + archive_file.split(".")[-2]

    # Extract the archive into releases_path
    tar_args = (remote_archive_path, releases_path)
    cmd2 = run("tar xvf {} --directory={}".format(*tar_args))

    # We done with the archive, so let's get ride of it
    cmd3 = run("rm {}".format(remote_archive_path))

    # The archive is consists of the directory web_static, so I had to mess
    # around with it to get its content moved to new_release_path, and finally
    # remove it, Please DO NOT ask me why I didn't compress the files directly
    # into the archive file, I was told to do it this way.
    cmd4 = run("mkdir -p {}".format(new_release_path))
    cmd5 = run("cp -r {}/* {}/".format(releases_path+"web_static",
                                       new_release_path))
    cmd6 = run("rm -rf {}".format(releases_path+"web_static"))

    cmd7 = run("ln -sf {} /data/web_static/current".format(new_release_path))

    commands = (
        cmd1,
        cmd2,
        cmd3,
        cmd4,
        cmd5,
        cmd6,
        cmd7
    )
    if all(commands):
        print("--- Deploy is done! ---")
    else:
        return False
