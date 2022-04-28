#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the web_static """

from fabric.api import local
import datetime


def do_pack():
    """ makes tgz compressed file """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file = local("tar -czvf versions/web_static_{}\.tgz web_static".format(now))
    if file:
        return("versions/web_static_{}".format(now))
    else:
        return None
