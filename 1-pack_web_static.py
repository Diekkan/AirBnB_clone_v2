#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the web_static """

from fabric.api import local
import datetime


def do_pack():
    """ makes tgz compressed file """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file = local(f"tar -czvf versions/web_static_{now}\.tgz web_static")
    if file:
        return(f"versions/web_static_{now}")
    else:
        return None
