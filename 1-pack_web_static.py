#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder of The
AirBnB Clone repo,
"""
from fabric.api import *
from datetime import datetime

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    curr_time = datetime.now()
    ver_time = curr_time.strftime("%Y%m%d%H%M%S")
    tar_path = "versions/web_static_{}.tgz".format(ver_time)

    r = local("tar czf {} web_static/".format(tar_path))

    if r.succeeded:
        return tar_path
    else:
        return None
